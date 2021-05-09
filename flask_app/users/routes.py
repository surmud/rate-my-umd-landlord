from flask import Blueprint, redirect, url_for, render_template, flash, request
from flask_login import current_user, login_required, login_user, logout_user

from .. import bcrypt
from ..forms import RegisterForm, LoginForm, UpdatePasswordForm, UpdateUsernameForm
from ..models import User

users = Blueprint("users", __name__)

@users.route('/users/<username>')
def account(username):
    username_form = UpdateUsernameForm()
    password_form = UpdatePasswordForm()

    if username_form.validate_on_submit():
        current_user.modify(username=username_form.username.data)
        current_user.save()
        return redirect(url_for('users.account'))

    if password_form.validate_on_submit():
        hashed = bcrypt.generate_password_hash(password_form.password.data).decode("utf-8")
        current_user.modify(password=hashed)
        current_user.save()
        return redirect(url_for('users.account'))

    return render_template('account.html', username_form=username_form, password_form=password_form)


@users.route('/login')
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    form = LoginForm()
    if form.validate_on_submit():
        user = User.objects(username=form.username.data).first()

        if user is not None and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for('users.account'))
        else:
            flash("Login Failed. Make sure you entered the right username/password")
            return redirect(url_for("users.login"))

    return render_template('login.html', form=form)


@users.route('/register')
def register():
    if current_user.is_authenticated:
        return redirect(url_for("index"))

    form = RegisterForm()
    if form.validate_on_submit():
        hashed = bcrypt.generate_password_hash(form.password.data).decode("utf-8")
        user = User(username=form.username.data, email=form.email.data, password=hashed)
        user.save()

        return redirect(url_for("users.login"))


    return render_template('register.html', form=form)
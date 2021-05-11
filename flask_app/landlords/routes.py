from flask import Blueprint, render_template, url_for, redirect, request, flash
from flask_login import current_user
from ..forms import LandlordReviewForm


landlords = Blueprint("landlords", __name__)

@landlords.route("/", methods=["GET", "POST"])
def index():
    form = LandlordReviewForm()

    
    return render_template("index.html", form = form)


@landlords.route('/landlords/<landlord_name>', methods = ["GET", "POST"])
def landlord(landlord_name):
    form = LandlordReviewForm()
    
    #show a form that lets the user rate the current landlord
    return render_template('landlord.html')
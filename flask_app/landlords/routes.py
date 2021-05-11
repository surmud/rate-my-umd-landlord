from flask import Blueprint, render_template, url_for, redirect, request, flash
from ..forms import LandlordReviewForm
from ..models import LandlordReview
from flask_login import current_user, login_required, login_user, logout_user

landlords = Blueprint("landlords", __name__)

@landlords.route("/", methods=["GET", "POST"])
def index():
    form = LandlordReviewForm()
    reviews = LandlordReview.objects()

    if form.validate_on_submit():
        review = LandlordReview(
            author = form.name.data,
            landlord_name = form.landlordName.data,
            location = form.address.data,
            rating = form.rating.data,
            review_content = form.landlordReview.data)

        review.save()
        return redirect(request.path)
  


    
    return render_template("index.html", form = form, current_user = current_user, reviews = reviews)


@landlords.route('/landlords/<landlord_name>', methods = ["GET", "POST"])
def landlord(landlord_name):
    form = LandlordReviewForm()
    
    #show a form that lets the user rate the current landlord
    return render_template('landlord.html')


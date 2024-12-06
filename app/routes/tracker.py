from flask import Blueprint, render_template

traker_bp = Blueprint('traker_bp', __name__)

@traker_bp.route('/')
def index():
    return render_template("base.html")

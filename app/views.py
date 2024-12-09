from flask import Blueprint, render_template


views = Blueprint('views', __name__)

@views.route('/')
def home():
    fruits = ['apple', 'banana', 'melon', 'watermelon']
    return 'Hlo'

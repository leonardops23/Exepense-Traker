from flask import Blueprint, render_template


views = Blueprint('views', __name__)

@views.route('/')
def home():
    fruits = ['apple', 'banana', 'melon', 'watermelon']
    return render_template('index.html', fruits=fruits)


@views.route('/login')
def login():
    return render_template('login.html')


@views.route('/register')
def register():
    return render_template('register.html')
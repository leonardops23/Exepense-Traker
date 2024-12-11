from flask import Blueprint, render_template


auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template('login.html', text="Helo")


@auth.route('/register')
def register():
    return render_template('register.html')


@auth.route('/logout')
def logout():
    return 'logout'
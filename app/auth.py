from flask import Blueprint, render_template, request


auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    data = request.form
    print(data)
    return render_template('login.html', text="Helo")


@auth.route('/register')
def register():
    return render_template('register.html')


@auth.route('/logout', methods=['GET', 'POST'])
def logout():
    return 'logout'

from flask import Blueprint, render_template, request


auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    data = request.form
    print(data)
    return render_template('login.html', text="Helo")


@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        print(request.form)
        # get info
        user1 = request.form.get('user1')
        email = request.form.get('email')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if password1 != password2:
            return 'Incorret password, try again!'
        print(f'{user1}, {email}, {password1}, {password2}')

    return render_template('register.html')


@auth.route('/logout')
def logout():
    return 'logout'

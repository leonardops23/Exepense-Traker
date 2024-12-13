from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    data = request.form
    print(data)  # Depuración: Imprime los datos del formulario en la consola
    return render_template('login.html', text="Hello")

@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('user1')
        email = request.form.get('email')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(username) < 2:
            flash('Username must be longer than 1 character.', 'danger')
        elif len(email) == 0:
            flash('please fill in the fields', 'danger')
        elif password1 != password2:
            flash('Passwords do not match.', 'danger')
        elif len(password1) < 6:
            flash('Password must be at least 6 characters long.', 'danger')
        else:
            flash('Registration successful!', 'success')

    return render_template('register.html')

@auth.route('/logout')
def logout():
    return 'You have been logged out.'

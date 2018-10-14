from flask import Flask, render_template, request, url_for, flash, redirect
from forms import SignupForm, LoginForm, SearchForm
from APIs.PixabayAPI import get_image_url
from APIs.WikiAPI import get_description

app = Flask(__name__)

# Move to config file and generate a new secret key later, put key in env variables
app.config['SECRET_KEY'] = 'a1db3c8a527d33eb2cba3821dac32950787f226c19cc479947f720306e867217'


@app.route('/signup', methods=['POST', 'GET'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('signup.html', title='Sign up', form=form)


@app.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@email.com' and form.password.data == 'password':
            flash(f'You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash(f'Login failed. Invalid username and/or password.', 'danger')
    return render_template('login.html', title='Log in', form=form)


@app.route('/', methods=['POST', 'GET'])
@app.route('/<user>', methods=['POST', 'GET'])
def home(user=None):
    form = SearchForm()
    if form.validate_on_submit():
        return redirect(url_for('home'))
    return render_template('home.html', user=user, form=form)


@app.route('/result', methods=['POST', 'GET'])
@app.route('/<user>/result', methods=['POST', 'GET'])
def result(user=None):
    form = SearchForm()
    if request.method == 'POST':
        search_text = request.form['search']
        if search_text != "":
            image_url = get_image_url(search_text)
            description = get_description(search_text)
            return render_template('home.html', image_url=image_url, description=description,
                                   search_text=search_text, user=user, title='Search result', form=form)


if __name__ == '__main__':
    app.run(debug=True)

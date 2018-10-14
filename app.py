from flask import Flask, render_template, request
import APIs.PixabayAPI
import APIs.WikiAPI


app = Flask(__name__)


@app.route('/signup')
def signup():
    return render_template('signup.html', title='Sign up')


@app.route('/login', methods=['POST', 'GET'])
def login():
    return render_template('login.html', title='Log in')


@app.route('/', methods=['POST', 'GET'])
@app.route('/<user>', methods=['POST', 'GET'])
def home(user=None):
    return render_template('home.html', user=user)


@app.route('/result', methods=['POST', 'GET'])
@app.route('/<user>/result', methods=['POST', 'GET'])
def result(user=None):

    if request.method == 'POST':
        search_text = request.form['search']
        if search_text != "":
            image_url = APIs.PixabayAPI.get_image_url(search_text)
            description = APIs.WikiAPI.get_description(search_text)
            return render_template('home.html', image_url=image_url,
                                   description=description, search_text=search_text, user=user, title='Search result')


if __name__ == '__main__':
    app.run(debug=True)

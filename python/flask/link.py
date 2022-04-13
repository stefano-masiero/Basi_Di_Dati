from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return """Hello, World! <br>
    Click <a href='/users/anonymous'>here</a> to continue."""


@app.route('/users/<username>')
def show_profile(username):
    users = ['alice', 'bob', 'charlie']
    if username in users:
        return 'Welcome to the web app, %s!' % username
    else:
        return 'Welcome to the web app, unregistered user!'

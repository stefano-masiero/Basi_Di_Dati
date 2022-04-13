from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/users/<username>')
def show_profile(username):
    users = ['alice', 'bob', 'charlie']
    if username in users:
        return render_template('profile.html',user=username)
    else:
        return render_template('profile.html',reg=users)

@app.route('/login',methods=['GET','POST'])
def login():
    user=request.form['user']
    return redirect(url_for('show_profile',username=user))
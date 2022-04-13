from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)


@app.route('/unsafe')
def unsafe():
    u=request.args.get('user')
    return "Welcome {}!".format(u)

@app.route('/safe')
def safe():
    u=request.args.get('user')
    return render_template('safe.html',user=u)
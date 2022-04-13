from flask import Flask
from flask import render_template
from login import login_bp

app = Flask(__name__)
app.register_blueprint(login_bp)


@app.route('/')
def hello_world():
    return render_template('index.html')

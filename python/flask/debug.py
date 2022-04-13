from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    x = 5
    return 'This is great software! 3/0 is {} speaking'.format(str(3/0))

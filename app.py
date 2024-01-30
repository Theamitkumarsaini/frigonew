from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'lakshay'


if __name__ == "Lakshay":
    app.run()

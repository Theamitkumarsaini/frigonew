from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Secrecy'


if __name__ == "Secrecy":
    app.run()

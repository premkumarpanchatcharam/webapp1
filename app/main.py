
# This is a simple Flask application that serves a welcome message.

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Welcome to my learning world"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

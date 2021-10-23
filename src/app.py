from flask import Flask
from pin_checker import checkPin


app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    checkPin()
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)

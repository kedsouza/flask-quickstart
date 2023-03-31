from flask import Flask
import tensorflow as tf
print("TensorFlow version:", tf.__version__)

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

if __name__ == '__main__':
    app.run()

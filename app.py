import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    message = "Hi, nice to see you" 
    return message

@app.route('/welcome')
def hello():
    return '2nd line on the page'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

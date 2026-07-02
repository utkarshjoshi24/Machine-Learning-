from flask import Flask

app = Flask(__name__)

@app.route("/")
def welcome():
    return f"Welcome to basic flask app"

@app.route("/index")
def index():
    return f"Welcome to the index page of flask app"

if __name__ == "__main__":
    app.run(debug=True)
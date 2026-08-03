from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/features")
def features():
    return render_template("features.html")


@app.route("/journey")
def journey():
    return render_template("journey.html")


@app.route("/tech")
def tech():
    return render_template("tech.html")



if __name__ == "__main__":
    app.run(debug=True, port=5002)
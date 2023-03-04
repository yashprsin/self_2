from flask import Flask, render_template
App = Flask(__name__)

@App.route("/")
def hello():
    return render_template('index.html')

@App.route("/about")
def yash():
    name = "yash"
    return render_template("about.html", name=name)


@App.route("/bootstrap")
def bootstrap():
    return render_template("bootstrap.html")

App.run(debug=True)

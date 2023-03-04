from flask import Flask, render_template
App = Flask(__name__)

@App.route("/")
def home():
    return render_template('index.html')

@App.route("/about")
def about():
    return render_template("about.html")

@App.route("/contact")
def contact():
    return render_template("contact.html")

@App.route("/post")
def post():
    return render_template("post.html")

App.run(debug=True)

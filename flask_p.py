from flask import Flask, render_template

skills_app = Flask(__name__)

@skills_app.route("/")
def home():
    return render_template("Home.html", t="Home", css_file="Home")

@skills_app.route("/about")
def about():
    return render_template("About.html", t="About", css_file="About")

@skills_app.route("/basie")
def basie():
    return render_template("Basie.html", t="Basie", css_file="Home")

@skills_app.route("/profile")
def profile():
    return render_template("profile.html", t="Profile", css_file="Home")

if __name__ == "__main__":
    skills_app.run(debug=True, host="0.0.0.0", port=3000)

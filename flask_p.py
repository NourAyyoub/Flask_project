from flask import Flask, render_template

skills_app = Flask(__name__)

pets = [
            {"id": 1, "name": "Nelly", "age": "5 weeks", "bio": "I am a tiny kitten rescued by the good people at Paws Rescue Center. I love squeaky toys and cuddles."},
            {"id": 2, "name": "Yuki", "age": "8 months", "bio": "I am a handsome gentle-cat. I like to dress up in bow ties."},
            {"id": 3, "name": "Basker", "age": "1 year", "bio": "I love barking. But, I love my friends more."},
            {"id": 4, "name": "Mr. Furrkins", "age": "5 years", "bio": "Probably napping."}, 
        ]

@skills_app.route("/")
def home():
    Users = {
                "Ayyoub":"Amsterdam", 
                "Mohammed":"London", 
                "Nour":"San Francisco", 
                "Abd Al-kareem":"Los Angeles"
            }
    
    return render_template("Home.html", t="Home", user = Users, css_file="Home")

@skills_app.route("/about")
def about():
    return render_template("About.html", t="About", css_file="About")

@skills_app.route("/basie")
def basie():
    return render_template("Basie.html", t="Basie", css_file="Home")

@skills_app.route("/profile")
def profile():
    return render_template("profile.html", t="Profile", css_file="Home")
"""
@skills_app.route("/details/<int:pet_id>")
def pet_details(pet_id):
    #View function for Showing Details of Each Pet. 
    pet = next((pet for pet in pets if pet["id"] == pet_id), None) 
    if pet is None: 
        abort(404, description="No Pet was Found with the given ID")
    return render_template("details.html", pet = pet)
"""
if __name__ == "__main__":
    skills_app.run(debug=True, host="0.0.0.0", port=3000)

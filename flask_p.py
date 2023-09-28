from flask import Flask, render_template, request
from forms import LoginForm, SignUpForm
from flask import session, redirect, url_for

skills_app = Flask(__name__)
skills_app.config['SECRET_KEY'] = 'dfewfew123213rwdsgert34tgfd1234trgf'
users3 = {
    "archie.andrews@email.com": "football4life",
    "veronica.lodge@email.com": "fashiondiva"
}
users = [
            {"id": 1, "full_name": "Pet Rescue Team", "email": "team@pawsrescue.com", "password": "adminpass"},
        ]
@skills_app.route("/")
def homepage():
    Users2 = {
                "Ayyoub":"Amsterdam", 
                "Mohammed":"London", 
                "Nour":"San Francisco", 
                "Abd Al-kareem":"Los Angeles"
            }
    
    return render_template("Home.html", t="Home", user = Users2, css_file="Home")

@skills_app.route("/about")
def about():
    return render_template("About.html", t="About", css_file="About")

@skills_app.route("/basie")
def basie():
    return render_template("Basie.html", t="Basie", css_file="Home")

@skills_app.route("/profile")
def profile():
    return render_template("profile.html", t="Profile", css_file="Home")

@skills_app.route("/login", methods=["POST", "GET"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = next((user for user in users if user["email"] == form.email.data and user["password"] == form.password.data), None)
        if user is None:
            return render_template("login.html", form = form, message = "Wrong Credentials. Please Try Again.")
        else:
            session['user'] = user
            return render_template("login.html", message = "Successfully Logged In!")
    return render_template("login.html", form = form)

    """  
     if form.validate_on_submit():
       print("Submitted and Valid.")
    elif form.errors:
        print(form.errors.items())
        print(form.email.errors)
        print(form.password.errors)
    
    
    if form.is_submitted():
        print("Submitted.")
    if form.validate():
        print("Valid.")

    if form.validate_on_submit():
       print("Submitted and Valid.")
       """ 
    """  if request.method == "POST":
        email = request.form["email"]
        password =request.form["password"]
        if email in users2 and users2[email] == password:
            return render_template("login.html", t="Login", css_file="Login", message ="Successfully Logged In")
        return render_template("login.html", t="Login", css_file="Login", message ="Incorrect Email or Password")
    return render_template("Login.html", t="Login", css_file="Login")"""

"""
@skills_app.route("/details/<int:pet_id>")
def pet_details(pet_id):
pets = [
            {"id": 1, "name": "Nelly", "age": "5 weeks", "bio": "I am a tiny kitten rescued by the good people at Paws Rescue Center. I love squeaky toys and cuddles."},
            {"id": 2, "name": "Yuki", "age": "8 months", "bio": "I am a handsome gentle-cat. I like to dress up in bow ties."},
            {"id": 3, "name": "Basker", "age": "1 year", "bio": "I love barking. But, I love my friends more."},
            {"id": 4, "name": "Mr. Furrkins", "age": "5 years", "bio": "Probably napping."}, 
        ]

    #View function for Showing Details of Each Pet. 
    pet = next((pet for pet in pets if pet["id"] == pet_id), None) 
    if pet is None: 
        abort(404, description="No Pet was Found with the given ID")
    return render_template("details.html", pet = pet)
"""

@skills_app.route("/signup", methods=["POST", "GET"])
def signup():
    """View function for Showing Details of Each Pet.""" 
    form = SignUpForm()
    if form.validate_on_submit():
        new_user = {"id": len(users3)+1, "full_name": form.full_name.data, "email": form.email.data, "password": form.password.data}
        users3.append(new_user)
        return render_template("Signup.html", message = "Successfully signed up")
    return render_template("Signup.html", form = form)

@skills_app.route("/logout")
def logout():
    if 'user' in session:
        session.pop('user')
    return redirect(url_for('homepage'))#return redirect(url_for('homepage', _scheme='https', _external=True))

 

if __name__ == "__main__":
    skills_app.run(debug=True, host="0.0.0.0", port=3000)

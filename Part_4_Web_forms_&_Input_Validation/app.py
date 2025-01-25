from flask import Flask,render_template,redirect,url_for,flash
from forms import SignupForm,LoginForm
app = Flask(__name__)
app.config["SECRET_KEY"] = "this_is_the_secret_key"

@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html",title="Home",page_class="home-page")

@app.route('/signup',methods=["GET","POST"])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        flash(f"Successfully registered {form.username.data}!!")
        return redirect(url_for("home"))
    return render_template("signup.html",title="Signup",form = form,page_class="signup-page")

@app.route('/login',methods=["GET","POST"])
def login():
    form = LoginForm()
    email = form.email.data
    pw= form.password.data
    if form.validate_on_submit():
        if email == "ab@c.com" and pw == 12345:
            flash (f"Logged in successfully!!")
            return redirect(url_for("home"))
        else:
            flash (f"Incorrect Email or password")

    return render_template("login.html",title="Login",form = form,page_class="login-page")

if __name__ == "__main__":
    app.run(debug=True)


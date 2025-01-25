from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "<h1> Welcome to the home page </h1>"

@app.route('/welcome/<name>')
def welcome_steve(name):
        return f"<h1> Hi {name.title()}, Welcome to our webpage </h1>"


if __name__=='__main__':
       app.run(debug=True)






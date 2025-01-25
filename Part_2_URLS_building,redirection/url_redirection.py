from flask import Flask , redirect , url_for 
import time

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1> Welcome to the home page </h1>"

@app.route('/pass')
def passed():
    return "<h1> Congrats! You have passed..."


@app.route('/fail')
def failed():
    return "<h1> Sorry , you have failed.."

@app.route('/score/<name>/<int:num>')
def score(name,num):
    if num < 30:
        time.sleep(1)
        #redirect user to the page fail
        return redirect(url_for("failed"))
    else:
        time.sleep(1)
        #redirect user to the page pass
        return redirect(url_for("passed"))
    

if __name__=='__main__':
       app.run(debug=True)

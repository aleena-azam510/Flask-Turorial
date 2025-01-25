from flask import Flask , redirect , url_for 
import time

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1> Welcome to the home page </h1>"

@app.route('/pass/<sname>/<int:marks>')
def passed(sname,marks):
    return f"<h1> Congrats!{sname} You have passed with {marks} marks..."


@app.route('/fail/<sname>/<int:marks>')
def failed(sname,marks):
    return f"<h1> Sorry {sname}, you have failed with {marks} marks.."

@app.route('/score/<name>/<int:num>')
def score(name,num):
    if num < 30:
        time.sleep(1)
        #redirect user to the page fail
        return redirect(url_for("failed",sname=name,marks=num))
    else:
        time.sleep(1)
        #redirect user to the page pass
        return redirect(url_for("passed",sname=name,marks=num))
    

if __name__=='__main__':
       app.run(debug=True)

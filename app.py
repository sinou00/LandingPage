# app.py
from flask import Flask, render_template, request, redirect, url_for
from flask import make_response
from flask_pymongo import PyMongo
import os


app = Flask(__name__, static_url_path='/static')
app.config["MONGO_URI"] =  "mongodb+srv://harisseyassine:winners2005@cluster0.0rwf9t8.mongodb.net/waitinglist"  # Replace with your MongoDB URI
mongo = PyMongo(app)



@app.route('/')
def index():
    return render_template('landingtest.html')

@app.route("/thanks")
def thanks_page():
    return render_template("thanks.html")  # Render the success page HTML


@app.route("/join_waitlist", methods=["POST"])
def join_waitlist():
    if request.method == "POST":
        
        email = request.form["email"]
        mongo.db.waitinglist.insert_one({"email": email})
        return redirect(url_for("thanks_page"))

if __name__ == '__main__':
    #app.run(debug=True)

    # for deployment with docker
    #app.run(host="0.0.0.0",port=8080) 

    # for deployment in heroku 
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)

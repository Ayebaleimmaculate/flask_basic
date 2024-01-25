# Creating my first flask app
from flask import Flask
#Creating an instance from the Flask class
app = Flask(__name__)

#working with the app decorator. starts with the @ symbol
#It takes in two parameters that is the path/url and the methods parameter

@app.route("/") # defines the path and method to be used and "/" defines methods to be used

#creating a route page for the app
def home():
    return "<h1>Ayebale Immaculate cohort 3 Semester two python flask </h1>"\
'<p>i enjoy code</p>'

@app.route("/about")
def about():
    return "<h2>flask basics </h2>"

#turning on the debug option
if __name__ =="_main_":
    app.run(debug=True)
import os
from flask import Flask, url_for, render_template, request, session, redirect

app = Flask(__name__)

app.secret_key="fadlfjh9843fherifnlkjfn3r"

@app.route('/')
def hello():
    return render_template("hello.html")

@app.route('/start')
def start():
    return render_template("start.html")
    
@app.route('/question1')
def question1():
	return render_template("question1.html")
	
@app.route('/question2', methods=["post"])
def question2():
	session["question1"]=request.form["sex"]
	return render_template("question2.html")
	
@app.route('/result', methods=["post"])
def question3():
	session["question2"]=request.form["role"]
	return render_template("result.html", person=guessPerson())
	
def guessPerson():
	"""Using values in session, guess who the user has in mind"""
	return "Barack Obama"
    
# @app.route('/#showedClickable')
# def showedClickable():
#     return render_template(
    
# def ftoc(ftemp):
#    return (ftemp-32.0)*(5.0/9.0)
# 
# @app.route('/ftoc/<ftempString>')
# def convertFtoC(ftempString):
#     ftemp = 0.0
#     try:
#         ftemp = float(ftempString)
#         ctemp = ftoc(ftemp)
#         return "In Farenheit: " + ftempString + " In Celsius " + str(ctemp) 
#     except ValueError:
#         return "Sorry.  Could not convert " + ftempString + " to a number"
# 
##def miles(miles):
##    return (miles/0.62137)
##
##@app.route('/milesToKm')
##def milesToKm():
##    return render_template('milesToKm.html')
##
##@app.route('/doMilesToKm')
##def doMilesToKm():
##    
##    try:
##        miles = float(request.args['miles'])
##        km = miles(miles)
##        return render_template('milesConvertResult.html',
##                               showMiles=miles,
##                               showKm=km)
##    
##    except ValueError:
##        return "bar"
##        return render_template('couldNotConvert.html',
##                               showMiles=miles)
##
if __name__ == "__main__":
    app.run(port=5000, debug=True)

import os
from flask import Flask, url_for, render_template, request

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template("hello.html")

@app.route('/start')
def start():
    return render_template("start.html")
    
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
    app.run(port=5000)

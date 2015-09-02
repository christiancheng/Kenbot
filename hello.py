import os
import datareader
from flask import Flask, url_for, render_template, request, session, redirect

app = Flask(__name__)

app.secret_key='fadlfjh9843fherifnlkjfn3r'

app.jinja_env.globals.update(len=len)

@app.route('/')
def hello():
    return render_template('hello.html')

@app.route('/start')
def start():
    return render_template('start.html')
    
@app.route('/question1')
def question1():
    return render_template('question1.html')
    
@app.route('/question2', methods=['post'])
def question2():
    session['question1']=request.form['sex']
    return render_template('question2.html')
    
@app.route('/question3', methods=["post"])
def question3():
    session['question2']=request.form['role']
    return render_template('question3.html')

@app.route('/question4', methods=['post'])
def question4():
    session['question3']=request.form['blackhair']
    return render_template('question4.html')
                           
@app.route('/question5', methods=['post'])
def question5():
    session['question4']=request.form['usesiPhone']
    return render_template('question5.html')

@app.route('/result',methods =['post'])
def result():
    session['question5']=request.form['noSports']
    return render_template('result.html', people=guessPerson())
    
def guessPerson():
    """Using values in session, guess who the user has in mind"""
    guess=datareader.People
    newGuess=[]
    for p in guess:
        if p.sex==session["question1"]:
            newGuess.append(p)
    guess=newGuess
    newGuess=[]
    for p in guess:
        if p.role==session["question2"]:
            newGuess.append(p)
    guess=newGuess
    newGuess=[]
    for p in guess:
        if p.blackhair==session["question3"]:
            newGuess.append(p)
    guess=newGuess
    newGuess=[]
    for p in guess:
        if p.usesiPhone==session["question4"]:
            newGuess.append(p)
    guess=newGuess
    newGuess=[]
    for p in guess:
        if p.noSports==session["question5"]:
            newGuess.append(p)
    print str(newGuess)
    return newGuess

if __name__ == "__main__":
    app.run(port=5000, debug=True)

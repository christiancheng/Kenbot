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

@app.route('/info')
def info():
    return render_template('info.html')
    
@app.route('/question1')
def question1():
    return render_template('question1.html')
    
@app.route('/question2', methods=['post'])
def question2():
    session['question1']=request.form['sex']
    return render_template('question2.html')
    
@app.route('/question3', methods=["post"])
def question3():
    session['question2']=request.form['student']
    return render_template('question3.html')

@app.route('/question4', methods=['post'])
def question4():
    session['question3']=request.form['blackhair']
    return render_template('question4.html')
                           
@app.route('/question5', methods=['post'])
def question5():
    session['question4']=request.form['usesiPhone']
    return render_template('question5.html')

@app.route('/question6', methods=['post'])
def question6():
    session['question5']=request.form['track']
    return render_template('question6.html')

@app.route('/question7', methods=['post'])
def question7():
    session['question6']=request.form['glasses']
    return render_template('question7.html')

@app.route('/question8', methods=['post'])
def question8():
    session['question7']=request.form['playedLeague']
    return render_template('question8.html')

@app.route('/question9', methods=['post'])
def question9():
    session['question8']=request.form['haveSiblings']
    return render_template('question9.html')

@app.route('/question10', methods=['post'])
def question10():
    session['question9']=request.form['basketball']
    return render_template('question10.html')

@app.route('/result',methods =['post'])
def result():
    session['question10']=request.form['noSports']
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
        if p.student==session["question2"]:
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
        if p.track==session["question5"]:
            newGuess.append(p)
    guess=newGuess
    newGuess=[]
    for p in guess:
        if p.glasses==session["question6"]:
            newGuess.append(p)
    guess=newGuess
    newGuess=[]
    for p in guess:
        if p.playedLeague==session["question7"]:
            newGuess.append(p)
    guess=newGuess
    newGuess=[]
    for p in guess:
        if p.haveSiblings==session["question8"]:
            newGuess.append(p)
    guess=newGuess
    newGuess=[]
    for p in guess:
        if p.basketball==session["question9"]:
            newGuess.append(p)
    guess=newGuess
    newGuess=[]
    for p in guess:
        if p.noSports==session["question10"]:
            newGuess.append(p)
    print str(newGuess)
    return newGuess

if __name__ == "__main__":
    app.run(port=5000, debug=True)

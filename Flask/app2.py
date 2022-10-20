### Intergrate HTMl
#### HTTP verb GET And POST 

from curses import use_env
from unittest import result
from flask import Flask,redirect,url_for,render_template,request

app=Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/success/<int:score>')
def success(score):
    # ress = ""
    # if score>=50:
    #     ress = 'PASS'
    # else:
    #     ress = "FAIL"
    return render_template('result.html',result = score)



@app.route('/fail/<int:score>')
def fail(score):
    return "The Person has failed and the marks is "+ str(score)

### Result checker
@app.route('/results/<int:marks>')
def results(marks):
    result=""
    if marks<50:
        result='fail'
    else:
        result='success'
    return redirect(url_for(result,score=marks))

@app.route('/submit',methods=['POST','GET'])
def submit():
    total_score = 0
    if request.method=='POST':
        science = float(request.form['science'])
        maths = float(request.form['maths'])
        c = float(request.form['c'])
        data_science = float(request.form['datascience'])
        total_score =(science+maths+c+data_science)/4
    ress=""
   
    return redirect(url_for('success',score = total_score))

if __name__=='__main__':
    app.run(debug=True)
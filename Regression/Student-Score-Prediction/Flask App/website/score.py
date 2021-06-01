from flask import Blueprint,render_template,request,redirect,flash,url_for
import pandas as pd
import numpy as np

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

score = Blueprint('score',__name__)

def getScore(hours):
    url = "http://bit.ly/w-data"
    student_data = pd.read_csv(url)
    X = student_data.loc[:,["Hours"]].values 
    Y = student_data.loc[:,['Scores']].values
    x_train,x_test,y_train,y_test = train_test_split(X,Y,random_state=0,test_size=0.2)
    reg = LinearRegression(fit_intercept=True)
    reg.fit(x_train,y_train)
    yourScore=reg.predict([[hours]])

    return yourScore



@score.route("/",methods=['GET', 'POST'])
def form():
    return render_template("index.html")

@score.route("/score",methods=['GET', 'POST'])
def student_score():
    if request.method == 'POST':
        hrs = float(request.form['hours'])
        y_score=getScore(hrs)
        f_score=round(y_score[0][0],2)
        if f_score>100:
            flash("Your Score go higher than 100% which is invalid")
            return render_template("index.html")    
        return render_template("score.html",score_per=f_score)
    else:
        return render_template("index.html")



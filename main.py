from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from flask_misaka import Misaka
import os
import pandas as pd
import dataAnalysis as da


filename = 'results.csv'

content = ""
with open("readme.md", "r") as f:
     content = f.read()


poll_data = {'Question':'How difficult is this class?',
             'fields':['Easy','Not so Easy','Average','Above average','Difficult']
                                  }

app = Flask(__name__)
bootstrap = Bootstrap(app)
Misaka(app)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/user/<name>')
def user(name):
    return render_template('user.html',name=name)


@app.route('/polls')
def polls():
    return render_template('polls.html',data=poll_data)


@app.route('/voted')
def voted():
    vote = request.args.get('field')

    res = open(filename,'a')
    res.write(vote + ',')
    res.close()
    return render_template('thankyou.html')


@app.route('/results')
def results():
    names, votes =  da.compute()
    html_text = da.bar_plot(names=names, votes=votes)
    return render_template('results.html',question=poll_data['Question'],names_votes=zip(names,votes),plot=html_text)


@app.route('/home')
def home():
    return render_template('home.html',text=content)


if __name__ == "__main__":
    app.run(debug=True)

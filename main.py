from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
import os


filename = 'results.csv'


poll_data = {'Question':'How difficult is this class?',
             'fields':['Easy','Not so Easy','Average','Above average','Difficult']
                                  }

app = Flask(__name__)
bootstrap = Bootstrap(app)

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


if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask , request
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy as sa
 
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = sa.Column(sa.Integer , primary_key = True)
    name = sa.Column(sa.Text)

with app.app_context():
    db.create_all()

@app.route('/registraion',methods = ['GET','POST'])
def index():
    return 'hello' + request.method

@app.route('/auth')
def about():
    return ('')

@app.errorhandler(404)
def page_not_found(e):
    return 'not  found' , 404

app.run(debug=True) 



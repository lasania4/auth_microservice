from flask import Flask , request
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy as sa
 
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = sa.Column(sa.Integer , primary_key = True)
    name = sa.Column(sa.Text)
    password = sa.Column(sa.Text ,nullable = False)
    test = sa.Column(sa.Text)

with app.app_context():
    db.create_all()

@app.route('/registraion',methods = ['GET','POST'])
def index():
    name = request.form.get('name')
    password = request.form.get('password')
    if not name or not password:
        return 'вы не ввели данные'
    user = User(name = name, password = password)
    db.session.add (user)
    db.session.commit ()
    return 'hello' + name

@app.route('/auth' ,methods = ['GET','POST'])
def about():
    name = request.form.get('name')
    password = request.form.get('password')
    if not name or not password:
        return 'вы не ввели данные'
    real_password = User.query.filter_by(name = name).first()
    if not real_password or password != real_password.password:
        return 'данные не совпадают'
    return 'ok'

#@app.route('/coincidence')
#def aboutus():
    

    




@app.errorhandler(404)
def page_not_found(e):
    return 'not  found' , 404

app.run(debug=True) 



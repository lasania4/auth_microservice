import sqlalchemy as sa
from flask import Flask, request
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class User(db.Model):
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.Text ,unique=True)
    password = sa.Column(sa.Text, nullable=False)
    test = sa.Column(sa.Text)


with app.app_context():
    db.create_all()


@app.route('/registration', methods=['GET','POST'])
def index():
    name = request.form.get('name')
    password = request.form.get('password')
    if not name or not password:
        return 'вы не ввели данные'
    user = User.query.filter_by(name = name).first()
    if user:
        return 'пользователь уже существует'
    user = User(name = name, password = password)
    db.session.add (user)
    db.session.commit ()
    return 'hello ' + name

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
if __name__ == "__main__":
    app.run(debug=True) 



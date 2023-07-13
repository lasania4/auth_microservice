import sqlalchemy as sa
import time
from flask import Flask, request
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from flask_cors import CORS

app = Flask(__name__)
app.config["SECRET_KEY"] = "verysecret"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)
CORS(app)

admin = Admin(app, url='/admin')


class User(db.Model):
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.Text, unique=True)
    password = sa.Column(sa.Text, nullable=False)
    test = sa.Column(sa.Text)


class Post(db.Model):
    id = sa.Column(sa.Integer, primary_key=True)
    title = sa.Column(sa.Text, nullable=False)
    content = sa.Column(sa.Text, nullable=False)
    published_time = sa.Column(sa.DateTime, default=func.now)


class Card(db.Model):
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.Text, nullable=False)
    description = sa.Column(sa.Text)
    price = sa.Column(sa.Text)
    is_active = sa.Column(sa.Boolean, default=True)


class Order(db.Model):
    id = sa.Column(sa.Integer, primary_key=True)
    card_id = sa.Column(sa.Integer, nullable=False)
    customer_name = sa.Column(sa.Text, nullable=False)
    phone_number = sa.Column(sa.Text, nullable=False)


class UserAdminView(ModelView):
    pass


class CardAdminView(ModelView):
    pass


admin.add_view(CardAdminView(Card, db.session))

admin.add_view(UserAdminView(User, db.session))

with app.app_context():
    db.create_all()


@app.route('/registration', methods=['GET', 'POST'])
def index():
    name = request.form.get('name')
    password = request.form.get('password')
    if not name or not password:
        return 'вы не ввели данные'
    user = User.query.filter_by(name=name).first()
    if user:
        return 'пользователь уже существует'
    user = User(name=name, password=password)
    db.session.add(user)
    db.session.commit()
    return 'hello ' + name


@app.route('/auth', methods=['GET', 'POST'])
def about():
    name = request.form.get('name')
    password = request.form.get('password')
    if not name or not password:
        return 'вы не ввели данные'
    real_password = User.query.filter_by(name=name).first()
    if not real_password or password != real_password.password:
        return 'данные не совпадают'
    return 'ok'


@app.post('/card')
def card():
    name = request.form.get('name')
    price = request.form.get('price')
    description = request.form.get('description')
    if not name:
        return 'no such data'
    card = Card(name=name, price=price, description=description)
    db.session.add(card)
    db.session.commit()
    return 'ok'


@app.get('/cards')
def cards():
    all_cards = Card.query.filter_by(is_active=True).all()
    response = []
    for el in all_cards:
        response.append({
            'id': el.id,
            'name': el.name,
            'description': el.description,
            "price": el.price
        })

    return response


@app.patch('/card')
def update_cards():
    id = request.form.get('id')
    name = request.form.get('name')
    description = request.form.get('description')
    price = request.form.get('price')
    if not id:
        return 'id not found'
    card = Card.query.filter_by(id=id).first()
    if not card:
        return 'card not found'
    card.name = name if 'name' in request.form else card.name
    db.session.commit()
    return 'ok'


@app.delete('/card')
def delete_card():
    id = request.form.get('id')
    if not id:
        return 'id not found'
    card = Card.query.filter_by(id=id).first()
    if not card:
        return 'card not found'
    db.session.delete(card)
    db.session.commit()


@app.post("/make_order")
def make_order():
    print(request.get_json())

    id_ = request.json.get("id")
    new_order = Order(
        card_id=id_,
        customer_name="Alexey",
        phone_number="+79992223344"
    )
    db.session.add(new_order)
    db.session.commit()
    return {
        "code": 0
    }


@app.errorhandler(404)
def page_not_found(e):
    return 'not  found', 404


if __name__ == "__main__":
    app.run(debug=True)

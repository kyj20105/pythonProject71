from pybo import db

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)
    user_id=db.Column(db.Integer, db.ForeignKey(
        'user.id', ondelete='CASCADE'), nullable=True, server_default='1')
    user=db.relationship('User', backref=db.backref('question_set'))


class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_id= db.Column(db.Integer, db.ForeignKey('question.id', ondelete='CASCADE'))
    question = db.relationship('Question', backref=db.backref('answer_set', ))
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey(
        'user.id', ondelete='CASCADE'), nullable=True, server_default='1')
    user = db.relationship('User', backref=db.backref('answer_set'))



class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    email=db.Column(db.String(120), unique=True, nullable=False)


class Drink(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name=db.Column(db.Text, nullable=False)
    decription=db.Column(db.Text, nullable=False)
    one_serving_kca=db.Column(db.Numeric, nullable=False)
    sodium_mg=db.Column(db.Numeric, nullable=False)
    saturated_fat_g=db.Column(db.Numeric, nullable=False)
    sugars_g=db.Column(db.Numeric, nullable=False)
    protien_g=db.Column(db.Numeric, nullable=False)
    caffeine=db.Column(db.Numeric, nullable=False)
    size_name=db.Column(db.Text, nullable=False)
    size_ml=db.Column(db.Text, nullable=False)
    size_fluid_ounce=db.Column(db.Text, nullable=False)



class Dessert(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name=db.Column(db.Text, nullable=False)
    decription=db.Column(db.Text, nullable=False)
    one_serving_kca=db.Column(db.Numeric, nullable=False)
    sodium_mg=db.Column(db.Numeric, nullable=False)
    saturated_fat_g=db.Column(db.Numeric, nullable=False)
    sugars_g=db.Column(db.Numeric, nullable=False)
    protien_g=db.Column(db.Numeric, nullable=False)
    caffeine=db.Column(db.Numeric, nullable=False)


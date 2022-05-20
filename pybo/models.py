from pybo import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

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


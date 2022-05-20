from flask import Blueprint, render_template
bp=Blueprint('main', __name__, url_prefix='/')

@bp.route('/hello')
def hello_pybo():
    return 'Hello, Pybo!'

@bp.route('/')
def index():
    return render_template('main/main.html')
@bp.route('/introduce')
def introduce():
    return render_template('introduce.html')
@bp.route('/drink')
def drink():
    return render_template('drink.html')
@bp.route('/dessert')
def dessert():
    return render_template('dessert.html')
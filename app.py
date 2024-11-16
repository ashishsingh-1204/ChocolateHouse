from flask import Flask, render_template, request, redirect, url_for
from models import db, SeasonalFlavor, Ingredient, CustomerSuggestion
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///chocolate_house.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()
    seed_data()

@app.route('/')
def index():
    return render_template('index.html')

def seed_data():
    if not SeasonalFlavor.query.first():
        flavors = [
            SeasonalFlavor(name="Pumpkin Spice", season="Fall"),
            SeasonalFlavor(name="Peppermint Mocha", season="Winter"),
        ]
        ingredients = [
            Ingredient(name="Cocoa Powder", quantity=200),
            Ingredient(name="Sugar", quantity=500),
        ]
        db.session.bulk_save_objects(flavors + ingredients)
        db.session.commit()
        app.logger.info("Database seeded with initial data")

@app.route('/flavors', methods=['GET', 'POST'])
def flavors():
    if request.method == 'POST':
        name = request.form['name']
        season = request.form['season']
        new_flavor = SeasonalFlavor(name=name, season=season)
        db.session.add(new_flavor)
        db.session.commit()
    flavors = SeasonalFlavor.query.all()
    return render_template('flavors.html', flavors=flavors)

@app.route('/inventory', methods=['GET', 'POST'])
def inventory():
    if request.method == 'POST':
        name = request.form['name']
        quantity = request.form['quantity']
        new_ingredient = Ingredient(name=name, quantity=quantity)
        db.session.add(new_ingredient)
        db.session.commit()
    ingredients = Ingredient.query.all()
    return render_template('inventory.html', ingredients=ingredients)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

@app.route('/suggestions', methods=['GET', 'POST'])
def suggestions():
    if request.method == 'POST':
        flavor = request.form['flavor']
        allergies = request.form['allergies']
        new_suggestion = CustomerSuggestion(flavor=flavor, allergies=allergies)
        db.session.add(new_suggestion)
        db.session.commit()
    suggestions = CustomerSuggestion.query.all()
    return render_template('suggestions.html', suggestions=suggestions)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

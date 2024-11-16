from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class SeasonalFlavor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    season = db.Column(db.String(20), nullable=False)

class Ingredient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

class CustomerSuggestion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    flavor = db.Column(db.String(100), nullable=False)
    allergies = db.Column(db.String(200))
# import necessary libraries
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import os

# create Flask app instance
app = Flask(__name__)

# configure the app to use SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///health_fitness_app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# create SQLAlchemy instance
db = SQLAlchemy(app)

# User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer)
    height = db.Column(db.Float)
    weight = db.Column(db.Float)
    workouts = db.relationship('Workout', backref='user', lazy=True)
    nutrition_logs = db.relationship('NutritionLog', backref='user', lazy=True)
    sleep_logs = db.relationship('SleepLog', backref='user', lazy=True)

# Workout model
class Workout(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    duration = db.Column(db.Integer)  # Duration in minutes
    type = db.Column(db.String(50))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

# NutritionLog model
class NutritionLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    meal_type = db.Column(db.String(50))
    calories = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

# SleepLog model
class SleepLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    duration = db.Column(db.Integer)  # Duration in minutes
    quality = db.Column(db.String(50))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


# create the database if it does not exist
if __name__ == '__main__':
    with app.app_context():
        if not os.path.exists('health_fitness_app.db'):
            db.create_all()
            print("Database created successfully!")
        else:
            print("Database already exists.")

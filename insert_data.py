from create import app, db, User, Workout, NutritionLog, SleepLog
from faker import Faker
import random
from datetime import datetime

fake = Faker()

# Function to generate random users
def create_users(num_users=10):
    users = []
    for _ in range(num_users):
        user = User(
            name=fake.name(),
            age=random.randint(18, 60),
            height=round(random.uniform(1.5, 2.0), 2),
            weight=round(random.uniform(50.0, 100.0), 2)
        )
        users.append(user)
    db.session.add_all(users)
    db.session.commit()

# Function to generate random workouts
def create_workouts(num_workouts=50):
    users = User.query.all()
    for _ in range(num_workouts):
        user = random.choice(users)
        workout = Workout(
            date=fake.date_between(start_date='-1y', end_date='today'),
            duration=random.randint(30, 120),
            type=random.choice(['Running', 'Cycling', 'Swimming', 'Gym', 'Yoga']),
            user_id=user.id
        )
        db.session.add(workout)
    db.session.commit()

# Function to generate random nutrition logs
def create_nutrition_logs(num_logs=100):
    users = User.query.all()
    for _ in range(num_logs):
        user = random.choice(users)
        nutrition_log = NutritionLog(
            date=fake.date_between(start_date='-1y', end_date='today'),
            meal_type=random.choice(['Breakfast', 'Lunch', 'Dinner', 'Snack']),
            calories=random.randint(100, 800),
            user_id=user.id
        )
        db.session.add(nutrition_log)
    db.session.commit()

# Function to generate random sleep logs
def create_sleep_logs(num_logs=100):
    # Get all users from the database
    users = User.query.all()

    # Create sleep logs for each user
    for _ in range(num_logs):
        # Choose a random user
        user = random.choice(users)

        # Create a sleep log with random data
        sleep_log = SleepLog(
            date=fake.date_between(start_date='-1y', end_date='today'),
            duration=random.randint(300, 600),  # Duration in minutes
            quality=random.choice(['Poor', 'Fair', 'Good', 'Excellent']),
            user_id=user.id
        )

        # Add the sleep log to the database session
        db.session.add(sleep_log)

    # Commit the changes to the database
    db.session.commit()

if __name__ == '__main__':
    with app.app_context():
        create_users()
        create_workouts()
        create_nutrition_logs()
        create_sleep_logs()
        print("Sample data inserted into the database.")

import unittest
from create import app, db, User, Workout, NutritionLog, SleepLog
from datetime import date

class HealthFitnessAppTestCase(unittest.TestCase):

    def setUp(self):
        """
        Set up a test client and create a new test database.
        This method is called before each test.
        """
        # Create a new Flask application context for testing
        self.app = app.test_client()
        with app.app_context():
            app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test_database.db'
            db.create_all()

    def tearDown(self):
        """
        Drop the test database after each test.
        This helps ensure each test is isolated and independent.
        """
        with app.app_context():
            db.session.remove()
            db.drop_all()


    def test_user_creation(self):
        """
        Test creating a user and asserting that the user is correctly added to the database.
        """
        with app.app_context():
            user = User(name="Test User", age=30, height=170, weight=70)
            db.session.add(user)
            db.session.commit()
            added_user = User.query.filter_by(name="Test User").first()
            self.assertIsNotNone(added_user)
            self.assertEqual(added_user.age, 30)

    def test_workout_logging(self):
        """
        Test logging a workout for a user and ensure that it's properly stored in the database.
        """
        with app.app_context():
            user = User(name="Workout User", age=25, height=165, weight=65)
            db.session.add(user)
            db.session.commit()
            workout = Workout(date=date.today(), duration=60, type="Running", user_id=user.id)
            db.session.add(workout)
            db.session.commit()
            logged_workout = Workout.query.filter_by(user_id=user.id).first()
            self.assertIsNotNone(logged_workout)
            self.assertEqual(logged_workout.type, "Running")

    def test_nutrition_log_entry(self):
        """
        Test adding a nutrition log entry for a user and validate its presence in the database.
        """
        with app.app_context():
            user = User(name="Nutrition User", age=28, height=160, weight=60)
            db.session.add(user)
            db.session.commit()
            nutrition_log = NutritionLog(date=date.today(), meal_type="Lunch", calories=500, user_id=user.id)
            db.session.add(nutrition_log)
            db.session.commit()
            logged_nutrition = NutritionLog.query.filter_by(user_id=user.id).first()
            self.assertIsNotNone(logged_nutrition)
            self.assertEqual(logged_nutrition.meal_type, "Lunch")

    def test_sleep_log_entry(self):
        """
        Test the functionality of adding a sleep log entry for a user and check its accuracy in the database.
        """
        with app.app_context():
            user = User(name="Sleep User", age=26, height=175, weight=80)
            db.session.add(user)
            db.session.commit()
            sleep_log = SleepLog(date=date.today(), duration=480, quality="Good", user_id=user.id)
            db.session.add(sleep_log)
            db.session.commit()
            logged_sleep = SleepLog.query.filter_by(user_id=user.id).first()
            self.assertIsNotNone(logged_sleep)
            self.assertEqual(logged_sleep.quality, "Good")

    def test_query_all_users(self):
        """
        Test querying all users from the database.
        This test checks if the query returns the correct number of user records.
        """
        with app.app_context():
            user1 = User(name="Query User 1", age=32, height=180, weight=75)
            user2 = User(name="Query User 2", age=29, height=165, weight=65)
            db.session.add_all([user1, user2])
            db.session.commit()
            users = User.query.all()
            self.assertEqual(len(users), 2)
            self.assertTrue(any(user.name == "Query User 1" for user in users))
            self.assertTrue(any(user.name == "Query User 2" for user in users))

if __name__ == '__main__':
    unittest.main()

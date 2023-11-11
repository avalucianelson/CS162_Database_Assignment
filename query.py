from create import app, db, User, Workout, NutritionLog, SleepLog
from sqlalchemy import func
from sqlalchemy import func

# Query to get all users
def get_all_users():
    users = User.query.all()
    for user in users:
        print(f"User: {user.name}, Age: {user.age}, Height: {user.height}, Weight: {user.weight}")

# Query to get workouts for a specific user
def get_workouts_for_user(user_id):
    workouts = Workout.query.filter_by(user_id=user_id).all()
    for workout in workouts:
        print(f"Date: {workout.date}, Duration: {workout.duration} minutes, Type: {workout.type}")

# Query to get average calories consumed per day for a specific user
def get_average_calories(user_id):
    avg_calories = db.session.query(func.avg(NutritionLog.calories)).filter(NutritionLog.user_id == user_id).scalar()
    print(f"Average Calories for User ID {user_id}: {avg_calories}")

# Query to get sleep patterns for a specific user
def get_sleep_patterns(user_id):
    sleep_logs = SleepLog.query.filter_by(user_id=user_id).all()
    for log in sleep_logs:
        print(f"Date: {log.date}, Duration: {log.duration} minutes, Quality: {log.quality}")

# Query to get users with poor sleep quality
def get_users_with_poor_sleep():
    users = User.query.join(SleepLog).filter(SleepLog.quality == 'Poor').all()
    for user in users:
        print(f"User: {user.name} has poor sleep quality.")

# Query to get all workouts
def get_all_workouts():
    workouts = Workout.query.all()
    for workout in workouts:
        print(f"User ID: {workout.user_id}, Date: {workout.date}, Duration: {workout.duration} minutes, Type: {workout.type}")


def get_nutrition_logs_for_user(user_id):
    logs = NutritionLog.query.filter_by(user_id=user_id).all()
    for log in logs:
        print(f"Date: {log.date}, Calories: {log.calories}, meal_type: {log.meal_type}")

# Query to get users with a BMI over 25
def get_users_with_high_bmi():
    users = User.query.filter(User.weight / func.pow((User.height/100), 2) > 25).all()
    for user in users:
        print(f"User: {user.name} has a BMI over 25.")


if __name__ == '__main__':
    with app.app_context():
        user_id = 1
        print("All Users:")
        get_all_users()

        print("\nWorkouts for User ID 1:")
        get_workouts_for_user(1)

        print("\nAverage Calories for User ID 1:")
        get_average_calories(1)

        print("\nSleep Patterns for User ID 1:")
        get_sleep_patterns(1)

        print("\nUsers with Poor Sleep Quality:")
        get_users_with_poor_sleep()

        print("\nAll Workouts:")
        get_all_workouts()

        print("\nNutrition Logs for User ID 1:")
        get_nutrition_logs_for_user(user_id)

        print("\nUsers with a BMI over 25:")
        get_users_with_high_bmi()



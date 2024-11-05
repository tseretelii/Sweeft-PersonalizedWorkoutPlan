# populate_data.py

from django.core.exceptions import ObjectDoesNotExist
from PersonalizedWorkoutPlanApp.models import AppUser, Muscle, Exercise, Workout, WorkoutPlan, Goal
from django.contrib.auth.hashers import make_password
import random

def run():
    print("Starting data population...")
    # Clear existing data to avoid duplication (optional)
    AppUser.objects.all().delete()
    Muscle.objects.all().delete()
    Exercise.objects.all().delete()
    Workout.objects.all().delete()
    WorkoutPlan.objects.all().delete()
    Goal.objects.all().delete()

    # Create AppUser instances
    try:
        user1 = AppUser.objects.create(
            username="user1",
            password=make_password("password1"),
            first_name="John",
            last_name="Doe",
            email="johndoe@example.com",
            weight=70,
            height=175,
            age=25,
            gender=AppUser.GenderChoices.MALE
        )

        user2 = AppUser.objects.create(
            username="user2",
            password=make_password("password2"),
            first_name="Jane",
            last_name="Smith",
            email="janesmith@example.com",
            weight=60,
            height=165,
            age=30,
            gender=AppUser.GenderChoices.FEMALE
        )

    except ObjectDoesNotExist:
        print("Users already exist, skipping creation")

    # Create Muscle instances
    muscles = ["Biceps", "Triceps", "Quadriceps", "Hamstrings", "Glutes", "Pectorals", "Deltoids", "Abs"]
    muscle_objects = []

    for muscle_name in muscles:
        muscle, created = Muscle.objects.get_or_create(muscle=muscle_name)
        muscle_objects.append(muscle)

    print(f"Created {len(muscle_objects)} muscles.")

    # Create Exercise instances
    exercises_data = [
        {
            "name": "Push Up",
            "exercise_type": Exercise.ExerciseType.STRENGTH_TRAINING,
            "description": "Push ups are great for upper body strength.",
            "instruction": "Keep your body straight and lower yourself to the ground.",
            "target_muscles": ["Pectorals", "Triceps", "Deltoids"]
        },
        {
            "name": "Squat",
            "exercise_type": Exercise.ExerciseType.STRENGTH_TRAINING,
            "description": "Squats strengthen the legs and core.",
            "instruction": "Keep your back straight and bend your knees.",
            "target_muscles": ["Quadriceps", "Glutes", "Hamstrings"]
        },
        {
            "name": "Running",
            "exercise_type": Exercise.ExerciseType.CARDIO,
            "description": "Running improves cardiovascular health.",
            "instruction": "Maintain a steady pace.",
            "target_muscles": ["Quadriceps", "Hamstrings", "Glutes"]
        }
    ]

    exercise_objects = []
    for exercise_data in exercises_data:
        exercise, created = Exercise.objects.get_or_create(
            name=exercise_data["name"],
            exercise_type=exercise_data["exercise_type"],
            description=exercise_data["description"],
            instruction=exercise_data["instruction"],
        )
        # Add target muscles
        exercise.target_muscles.set([muscle for muscle in muscle_objects if muscle.muscle in exercise_data["target_muscles"]])
        exercise_objects.append(exercise)

    print(f"Created {len(exercise_objects)} exercises.")

    # Create Workout instances for each user
    workouts = [
        {
            "user": user1,
            "exercise": exercise_objects[0],  # Push Up
            "repetition": 15,
            "workout_set": 3,
            "duration_minutes": 10
        },
        {
            "user": user1,
            "exercise": exercise_objects[1],  # Squat
            "repetition": 20,
            "workout_set": 4,
            "duration_minutes": 15
        },
        {
            "user": user2,
            "exercise": exercise_objects[2],  # Running
            "distance": 5,
            "duration_minutes": 30
        }
    ]

    workout_objects = []
    for workout_data in workouts:
        workout, created = Workout.objects.get_or_create(
            user=workout_data["user"],
            exercise=workout_data["exercise"],
            repetition=workout_data.get("repetition"),
            workout_set=workout_data.get("workout_set"),
            distance=workout_data.get("distance"),
            duration_minutes=workout_data.get("duration_minutes")
        )
        workout_objects.append(workout)

    print(f"Created {len(workout_objects)} workouts.")

    # Create WorkoutPlan instances
    workout_plan1, created = WorkoutPlan.objects.get_or_create(
        user=user1,
        goal="Build upper body strength",
        frequency=3,
        daily_session_duration=45
    )
    workout_plan1.workout_list.set(workout_objects[:2])  # Assign first two workouts
    workout_plan2, created = WorkoutPlan.objects.get_or_create(
        user=user2,
        goal="Improve cardio endurance",
        frequency=4,
        daily_session_duration=60
    )
    workout_plan2.workout_list.set(workout_objects[2:])  # Assign last workout

    print(f"Created 2 workout plans.")

    # Create Goal instances
    goals = [
        {"user": user1, "goal": "Gain muscle mass"},
        {"user": user2, "goal": "Increase stamina"}
    ]

    for goal_data in goals:
        Goal.objects.get_or_create(user=goal_data["user"], goal=goal_data["goal"])

    print("Data population complete.")

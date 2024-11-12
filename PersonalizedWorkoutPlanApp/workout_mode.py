import time

class WorkoutMode:
    def start_workout(workout):
        print(f"This is my function: {workout.data}")
        workout_info = workout.data
        duration = workout_info['duration_minutes']
        time.sleep(duration)
        print(f"duration of the workout {duration}")
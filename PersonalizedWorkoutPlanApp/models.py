from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

# Note that the fields are designed for the metric system.

class AppUser(AbstractUser):
    class GenderChoices(models.TextChoices):
        MALE = "MALE"
        FEMALE = "FEMALE"

    weight = models.SmallIntegerField(validators=[MinValueValidator(1)])
    height = models.SmallIntegerField(validators=[MinValueValidator(1)])
    age = models.SmallIntegerField(validators=[MinValueValidator(16)])
    gender = models.CharField(max_length= 6,choices=GenderChoices.choices)

class Muscle(models.Model):
    muscle = models.CharField(max_length=50)

    def __str__(self):
        return self.muscle


class Exercise(models.Model):
    class ExerciseType(models.TextChoices):
        CARDIO = 'Cardio',
        STRENGTH_TRAINING = 'Strength Training',
        FLEXIBILITY = 'Flexibility',
    
    name = models.CharField(max_length=50)
    exercise_type = models.CharField(max_length=20, choices=ExerciseType.choices)
    description = models.TextField()
    instruction = models.TextField()
    target_muscles = models.ManyToManyField(Muscle)
    
    def __str__(self):
        return self.name

class Workout(models.Model):#  This class represents a user's ability to create a single workout within a workout plan. 
                            #  For example, a user can choose running and specify how long they want to run, 
                            #  or define the number of sets for an exercise, and so on.
    user = models.ForeignKey(AppUser, on_delete= models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete = models.CASCADE, related_name='exercise')
    distance = models.SmallIntegerField(null=True)
    duration_minutes = models.SmallIntegerField(null=True)
    repetition = models.SmallIntegerField(null=True)
    workout_set = models.SmallIntegerField(null=True)

    def __str__(self):
        return self.exercise.name




class WorkoutPlan(models.Model):
    user = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    goal = models.TextField()
    frequency = models.SmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(7)])
    workout_list = models.ManyToManyField(Workout)
    daily_session_duration = models.SmallIntegerField()

    def __str__(self):
        return self.goal


class Goal(models.Model):
    user = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    goal = models.TextField()

    def __str__(self):
        return self.goal
from rest_framework import serializers
from .models import *

class AppUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppUser
        fields = [
            "first_name",
            "last_name",
            "email",
            "password",
            "weight",
            "height",
            "age",
            "gender",
        ]

class MuscleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Muscle
        fields = "__all__"

class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = "__all__"

class WorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workout
        fields = "__all__"

class WorkoutPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workout
        fields = "__all__"

class GoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goal
        fields = "__all__"
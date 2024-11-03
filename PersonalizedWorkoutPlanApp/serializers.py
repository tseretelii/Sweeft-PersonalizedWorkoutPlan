from rest_framework import serializers
from .models import *

class AppUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppUser
        fields = [
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
            "password",
            "weight",
            "height",
            "age",
            "gender",
        ]
        extra_kwargs = {            # By Adding This code,
            'password': {           # password becomes write only,
                'write_only': True  # it does not appear on get request
            }
        }

    def create(self, validated_data):
        user = AppUser(
            username=validated_data['username'],
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name'],
            email = validated_data['email'],
            weight = validated_data['weight'],
            height = validated_data['height'],
            age = validated_data['age'],
            gender = validated_data['gender'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

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
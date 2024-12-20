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
    
    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.weight = validated_data.get('weight', instance.weight)
        instance.height = validated_data.get('height', instance.height)
        instance.age = validated_data.get('age', instance.age)
        instance.gender = validated_data.get('gender', instance.gender)

        if 'password' in validated_data:
            instance.set_password(validated_data['password'])
        instance.save()
        return instance

class MuscleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Muscle
        fields = "__all__"

class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = "__all__"

class WorkoutSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())# With this code you don’t need to explicitly pass the user field in the request body when creating or updating objects.
                                                                            # The user field will be populated automatically by Django REST Framework based on the authenticated user.

    class Meta:
        model = Workout
        fields = "__all__"

class WorkoutPlanSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    
    class Meta:
        model = Workout
        fields = "__all__"

class GoalSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Goal
        fields = "__all__"
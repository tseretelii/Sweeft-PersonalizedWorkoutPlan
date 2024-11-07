from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from .models import *
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
# Create your views here.

class AppUserViewSet(viewsets.ModelViewSet):
    queryset = AppUser.objects.all()
    serializer_class = AppUserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MuscleViewSet(viewsets.ModelViewSet):
    queryset = Muscle.objects.all()
    serializer_class = MuscleSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class ExerciseViewSet(viewsets.ModelViewSet):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class WorkoutViewSet(viewsets.ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer
    permission_classes = [IsAuthenticated]

class WorkoutPlanViewSet(viewsets.ModelViewSet):
    queryset = WorkoutPlan.objects.all()
    serializer_class = WorkoutPlanSerializer
    permission_classes = [IsAuthenticated]

class GoalViewSet(viewsets.ModelViewSet):
    queryset = Goal.objects.all()
    serializer_class = GoalSerializer
    permission_classes = [IsAuthenticated]

class CreateMyWorkOutPlan(APIView): # this view creates a Workout plan for a user based on their specific needs and conditions
    def post(self, request):
        goal = request.data['goal']
        n_times_week = request.data['number_of_times_a_week']
        workout_length = request.data['workout_length']

        # return Response({'respnse': [goal, n_times_week, workout_length]})
        if goal == 'get in shape':
            query_set = Exercise.objects.filter(exercise_type = Exercise.ExerciseType.CARDIO)
            
            print(query_set)
            query_set_for_workout = Workout.objects.create(
                user = AppUser.objects.first(),
                exercise = query_set.first(),
                distance = 5,
                duration_minutes = workout_length
            )
            print(query_set_for_workout)
            serializer_exercise = ExerciseSerializer(query_set[0]) # because it has one object in the queryset
            serializer_workout = WorkoutSerializer(query_set_for_workout)
            return Response({'exercises': serializer_exercise.data, 'workout': serializer_workout.data})
        

# class CreateMyWorkOutPlan(APIView): # this is just me messing arount with the functions and serializations
#     def post(self, request):
#         goal = request.data['goal']
#         n_times_week = request.data['number_of_times_a_week']
#         workout_length = request.data['workout_length']

#         if goal == 'get in shape':
#             query_set = Exercise.objects.filter(exercise_type=Exercise.ExerciseType.CARDIO)
#             if query_set.count() < 2:
#                 print(query_set.count())

#             serializer_exercise = ExerciseSerializer(query_set[0])
#             serializer_workout = WorkoutSerializer(Workout.objects.get(id=10))
            
#             app_user = AppUser.objects.all()
#             serializer_app_user = AppUserSerializer(app_user, many=True)
            
#             return Response({
#                 'exercises': serializer_exercise.data,
#                 'workout': serializer_workout.data,
#                 'rand_data': serializer_app_user.data
#             })


class MyWorkouts(APIView):
    def get(self, request):
        user_workouts = Workout.objects.prefetch_related( # by adding prefetch_related we optimize sql queries by joining tables
            'exercise',
            'exercise__target_muscles'
        ).filter(user = request.user)
        if user_workouts.count() < 2:
            workout_serializer = WorkoutSerializer(user_workouts)
            return Response({'MyWorkouts': workout_serializer.data})
        workout_serializer = WorkoutSerializer(user_workouts, many = True)
        return Response({'MyWorkouts': workout_serializer.data})
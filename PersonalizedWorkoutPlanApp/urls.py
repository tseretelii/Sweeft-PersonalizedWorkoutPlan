"""
URL configuration for PersonalizedWorkoutPlan project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'Appusers', AppUserViewSet)
router.register(r'Muscles', MuscleViewSet)
router.register(r'Exercises', ExerciseViewSet)
router.register(r'Workouts', WorkoutViewSet)
router.register(r'WorkoutPlans', WorkoutPlanViewSet)
router.register(r'Goals', GoalViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('create-my-exercise/', CreateMyWorkOutPlan.as_view()),
    path('MyWorkouts/', MyWorkouts.as_view()),
]
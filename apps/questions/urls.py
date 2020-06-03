
from django.urls import path, include
from .views import *

urlpatterns = [
    path('tasks/', tasks_list, name = 'tasks-list'),
    path('tasks/<int:pk>', questions_list, name = 'questions-list')
]
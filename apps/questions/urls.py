
from django.urls import path, include
from .views import *

urlpatterns = [
    path('tasks/', tasks_list, name = 'tasks-list'),
    path('tasks/<int:pk>/all', questions_list, name = 'questions-list'),
    path('tasks/<int:pk>/firstmath', firstmath_list, name = 'firstmath-list'),
    path('tasks/<int:pk>/secondmath', secondmath_list, name = 'secondmath-list'),
    path('tasks/<int:pk>/firstrussia', firstrussia_complement_list, name = 'firstrussia-list'),
    path('tasks/<int:pk>/secondrussia', secondrussia_reading_list, name = 'secondrussia-list'),
    path('tasks/<int:pk>/thirdrussia', thirdrussia_grammar_list, name = 'thirdrussia-list')
]

from django.urls import path

from .views import *

urlpatterns = [
    path('tasks/', tasks_list, name = 'tasks-list'),
    path('tasks/<int:pk>/all', questions_list, name = 'questions-list'),
    path('tasks/<int:pk>/mathone', firstmath_list, name = 'firstmath-list'),
    path('tasks/<int:pk>/mathtwo', secondmath_list, name = 'secondmath-list'),
    path('tasks/<int:pk>/analogy', firstrussia_complement_list, name = 'firstrussia-list'),
    path('tasks/<int:pk>/reading', secondrussia_reading_list, name = 'secondrussia-list'),
    path('tasks/<int:pk>/grammar', thirdrussia_grammar_list, name = 'thirdrussia-list')
]

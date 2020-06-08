from django.shortcuts import render

from .models import *


def tasks_list(request):
    tasks = Introduction.objects.all()
    return render(request, 'index.html', context={'tasks': tasks})

def questions_list(request, pk):
    task = Introduction.objects.get(pk = pk)
    all_questions = task.question.all()
    if request.method == 'POST':
        for i in range(1, 3):
            answers = request.POST.get(str(i))
            print(i)
            print(answers)
        return render(request, 'tasks/question.html', locals())
    else:
        return render(request, 'tasks/question.html', locals())
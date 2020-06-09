from django.shortcuts import render

from .models import *


def tasks_list(request):
    all_tasks = Introduction.objects.all()
    return render(request, 'tasks/task.html', locals())

def questions_list(request, pk):
    answered = False
    task = Introduction.objects.get(pk = pk)
    all_questions = task.question.all()
    last_question = task.question.last()
    if request.method == 'POST':
        answered = True 
        for i in range(1, last_question.номер + 1):
            answers = request.POST.get(str(i))
            current_question = task.question.get(номер = i)
            объяснение = current_question.объяснение
            if answers == current_question.правильный_вариант:
                task.балл += 1
        return render(request, 'tasks/explanation.html', locals())
    else:
        return render(request, 'tasks/question.html', locals())
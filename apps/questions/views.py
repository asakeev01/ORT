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
            answer = request.POST.get(str(i))
            current_question = task.question.get(номер = i)
            answer_model = Answer.objects.get(вопрос = current_question)
            right_answer = current_question.answer.правильный_вариант
            answer_model.отмеченный_вариант = answer
            answer_model.save()
            объяснение = current_question.answer.объяснение
            if answer_model == right_answer:
                task.балл += 1
        return render(request, 'tasks/explanation.html', locals())
    else:
        return render(request, 'tasks/question.html', locals())
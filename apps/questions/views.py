from django.shortcuts import render

from .models import *


def tasks_list(request):
    all_tasks = Introduction.objects.all()
    return render(request, 'tasks/task.html', locals())

def questions_list(request, pk):
    is_image = False 
    is_answered = False
    task = Introduction.objects.get(pk = pk)
    all_questions = task.question.all()
    last_question = task.question.order_by('номер').last()
    if request.method == 'POST':
        if request.user.is_authenticated:
            profile = request.user.profile
            review = Review.objects.create(профайл = profile)
        else:
            review = Review.objects.create()
        is_answered = True
        review.введение.add(task) 
        for i in range(1, last_question.номер + 1):
            try:
                current_question = task.question.get(номер = i)
                answer = request.POST.get(str(i))
                answer_model = Answer.objects.create(просмотр = review)
                answer_model.вопрос = current_question
                answer_model.отмеченный_вариант = answer
                answer_model.save()
                right_answer = current_question.правильный_вариант
                объяснение = current_question.объяснение
                if answer_model.отмеченный_вариант == right_answer:
                    review.балл += 1
                review.save()
            except:
                pass
        answers = review.answer.all()
        return render(request, 'tasks/explanation.html', locals())
    else:
        return render(request, 'tasks/all_questions.html', locals())

def firstmath_list(request, pk):
    is_image = False
    is_answered = False
    task = Introduction.objects.get(pk = pk)
    all_questions = task.question.filter(номер__lte = 30)
    last_question = all_questions.order_by('номер').last()
    if request.method == 'POST':
        if request.user.is_authenticated:
            profile = request.user.profile
            review = Review.objects.create(профайл = profile)
        else:
            review = Review.objects.create()
        is_answered = True 
        review.введение.add(task)
        for i in range(1, last_question.номер + 1):
            try:
                current_question = task.question.get(номер = i)
                answer = request.POST.get(str(i))
                answer_model = Answer.objects.create(просмотр = review)
                answer_model.вопрос = current_question
                answer_model.отмеченный_вариант = answer
                answer_model.save()
                right_answer = current_question.правильный_вариант
                объяснение = current_question.объяснение
                if answer_model.отмеченный_вариант == right_answer:
                    review.балл += 1
            except:
                pass
        answers = review.answer.all()
        return render(request, 'tasks/explanation.html', locals())
    else:
        return render(request, 'tasks/firstmath_questions.html', locals())

def secondmath_list(request, pk):
    is_answered = False 
    task = Introduction.objects.get(pk = pk)
    all_questions = task.question.filter(номер__gt = 30, номер__lte = 90)
    last_question = all_questions.order_by('номер').last()
    if request.method == 'POST':
        if request.user.is_authenticated:
            profile = request.user.profile
            review = Review.objects.create(профайл = profile)
        else:
            review = Review.objects.create()
        is_answered = True 
        for i in range(31, last_question.номер + 1):
            try:
                current_question = task.question.get(номер = i)
                answer = request.POST.get(str(i))
                answer_model = Answer.objects.create(просмотр = review)
                answer_model.вопрос = current_question
                answer_model.отмеченный_вариант = answer
                answer_model.save()
                right_answer = current_question.правильный_вариант
                объяснение = current_question.объяснение
                if answer_model.отмеченный_вариант == right_answer:
                    review.балл += 1
            except:
                pass
        answers = review.answer.all()
        return render(request, 'tasks/explanation.html', locals())
    else:
        return render(request, 'tasks/secondmath_questions.html', locals())

def firstrussia_complement_list(request, pk):
    is_answered = False 
    task = Introduction.objects.get(pk = pk)
    all_questions = task.question.filter(номер__gt = 90, номер__lte = 120)
    last_question = all_questions.order_by('номер').last()
    if request.method == 'POST':
        if request.user.is_authenticated:
            profile = request.user.profile
            review = Review.objects.create(профайл = profile)
        else:
            review = Review.objects.create()
        is_answered = True 
        for i in range(61, last_question.номер + 1):
            try:
                current_question = task.question.get(номер = i)
                answer = request.POST.get(str(i))
                answer_model = Answer.objects.create(просмотр = review)
                answer_model.вопрос = current_question
                answer_model.отмеченный_вариант = answer
                answer_model.save()
                right_answer = current_question.правильный_вариант
                объяснение = current_question.объяснение
                if answer_model.отмеченный_вариант == right_answer:
                    review.балл += 1
            except:
                pass
        answers = review.answer.all()
        return render(request, 'tasks/explanation.html', locals())
    else:
        return render(request, 'tasks/firstrussia_complement.html', locals())

def secondrussia_reading_list(request, pk):
    is_answered = False 
    task = Introduction.objects.get(pk = pk)
    all_questions = task.question.filter(номер__gt = 120, номер__lte = 150)
    last_question = all_questions.order_by('номер').last()
    if request.method == 'POST':
        if request.user.is_authenticated:
            profile = request.user.profile
            review = Review.objects.create(профайл = profile)
        else:
            review = Review.objects.create()
        is_answered = True 
        for i in range(121, last_question.номер + 1):
            try:
                current_question = task.question.get(номер = i)
                answer = request.POST.get(str(i))
                answer_model = Answer.objects.create(просмотр = review)
                answer_model.вопрос = current_question
                answer_model.отмеченный_вариант = answer
                answer_model.save()
                right_answer = current_question.правильный_вариант
                объяснение = current_question.объяснение
                if answer_model.отмеченный_вариант == right_answer:
                    review.балл += 1
            except:
                pass
        answers = review.answer.all()
        return render(request, 'tasks/explanation.html', locals())
    else:
        return render(request, 'tasks/secondrussia_reading.html', locals())

def thirdrussia_grammar_list(request, pk):
    is_answered = False 
    task = Introduction.objects.get(pk = pk)
    all_questions = task.question.filter(номер__gt = 150, номер__lte = 180)
    last_question = all_questions.order_by('номер').last()
    if request.method == 'POST':
        if request.user.is_authenticated:
            profile = request.user.profile
            review = Review.objects.create(профайл = profile)
        else:
            review = Review.objects.create()
        is_answered = True 
        for i in range(151, last_question.номер + 1):
            try:
                current_question = task.question.get(номер = i)
                answer = request.POST.get(str(i))
                answer_model = Answer.objects.create(просмотр = review)
                answer_model.вопрос = current_question
                answer_model.отмеченный_вариант = answer
                answer_model.save()
                right_answer = current_question.правильный_вариант
                объяснение = current_question.объяснение
                if answer_model.отмеченный_вариант == right_answer:
                    review.балл += 1
            except:
                pass
        answers = review.answer.all()
        return render(request, 'tasks/explanation.html', locals())
    else:
        return render(request, 'tasks/thirdrussia_grammar.html', locals())
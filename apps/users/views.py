from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

from apps.questions.models import Review


def login(request):
	if request.method == 'POST':
		if 'signing' in request.POST:
			# email = request.POST['email']
			username = request.POST['username']
			password = request.POST['password']
			user = auth.authenticate(username=username, password=password)
			if user is not None:
				auth.login(request, user)
				return redirect('/tasks/')
			else:
				messages.error(request, 'Пользователь не найден')
				return redirect('login')
		elif 'signup' in request.POST:
			username = request.POST['username']
			password = request.POST['password']
			if User.objects.filter(username=username).exists():
				messages.info(request, 'Имя занято')
				return redirect('register')
			else:
				user = User.objects.create_user(password=password, username=username)
				user.save()
				auth.login(request, user)
				return redirect('/tasks/')
	else:
		return render(request, 'users/login.html')


def logout(request):
	auth.logout(request)
	return redirect('/tasks/')


def register(request):
	if request.method == 'POST':
		if 'signup' in request.POST:
			username = request.POST['username']
			# email = request.POST['email']
			password = request.POST['password']
			if User.objects.filter(username=username).exists():
				messages.info(request, 'Имя занято')
				return redirect('register')
			else:
				user = User.objects.create_user(password=password, username=username)
				user.save()
				auth.login(request, user)
				return redirect('/tasks/')
		elif 'signing' in request.POST:
			# email = request.POST['email']
			username = request.POST['username']
			password = request.POST['password']
			user = auth.authenticate(username=username, password=password)
			if user is not None:
				auth.login(request, user)
				return redirect('/tasks/')
			else:
				messages.error(request, 'Пользователь не найден')
				return redirect('login')
	else:
		return render(request, 'users/register.html')


def review_list(request):
	user = request.user
	profile = user.profile
	reviews = profile.review.all()
	for review in reviews:
		answers = review.answer.all()
	return render(request, 'tasks/review.html', locals())

def review_detail(request, pk):
	profile = request.user.profile
	is_answered = True
	review = Review.objects.get(pk = pk)
	print(review.балл)
	answers = review.answer.all()
	return render(request, 'tasks/explanation.html', locals())
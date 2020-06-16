from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages


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
				messages.error(request, 'invalid credentials')
				return redirect('login')
		elif 'signup' in request.POST:
			username = request.POST['username']
			password = request.POST['password']
			if User.objects.filter(username=username).exists():
				messages.info(request, 'Username taken')
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
				messages.info(request, 'Username taken')
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
				messages.error(request, 'invalid credentials')
				return redirect('login')
	else:
		return render(request, 'users/register.html')


def profile(request):
	user = request.user
	profile = request.user.profile
	tasks = profile.tasks.all()
	print(tasks) 
	for task in tasks:
		questions = task.question.all()
	print(tasks)
	return render(request, 'users/profile.html', locals())
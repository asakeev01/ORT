from django.urls import path

from . import views

urlpatterns = [
	path('register/', views.register, name='register'),
	path('login/', views.login, name='login'),
	path('logout/', views.logout, name='logout'),
	path('review/', views.review_list, name='review'),
	path('review/<int:pk>/', views.review_detail, name='review_detail')
]
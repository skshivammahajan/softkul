from django.urls import path
from . import views

urlpatterns = [
	path('', views.task, name="list"),
	path('update/<str:pk>/', views.updateTask, name="update_task"),
	path('delete/<str:pk>/', views.deleteTask, name="delete"),
]
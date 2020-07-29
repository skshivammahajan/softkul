from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse

from .models import *
from .forms import *


@login_required(login_url='login')
def task(request):
	tasks = Task.objects.all()

	form = TaskForm()

	if request.method == 'POST':
		form = TaskForm(request.POST)
		# form.added_by = User.objects.get(id=request.user.id)

		if form.is_valid():
			# instance = form.save(commit=False)
			# instance.added_by = request.user

			form.save()
		return redirect('/task')

	context = {'tasks': tasks, 'form': form}
	return render(request, 'tasks/list.html', context)


@login_required(login_url='login')
def updateTask(request, pk):
	task = Task.objects.get(id=pk)

	form = TaskForm(instance=task)

	if request.method == 'POST':
		form = TaskForm(request.POST, instance=task)
		if form.is_valid():
			form.save()
			return redirect('/task')

	context = {'form':form}

	return render(request, 'tasks/update_task.html', context)


@login_required(login_url='login')
def deleteTask(request, pk):
	item = Task.objects.get(id=pk)

	if request.method == 'POST':
		item.delete()
		return redirect('/task')

	context = {'item':item}
	return render(request, 'tasks/delete.html', context)




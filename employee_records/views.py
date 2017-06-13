from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User, Group
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic

from .models import Task, Employee

# Create your views here.
def index(request):
		
	return render(request, 'employee_records/index.html')



def new_tasks(request):
	employee = Employee.objects.filter(user=request.user)
	user_tasks = Task.objects.filter(status='n', assign_to_employee=employee)
	return render(request, 'employee_records/new_tasks.html', {'user_tasks':user_tasks})

def task_detail(request, task_id):
	task = get_object_or_404(Task, pk=task_id)
	task_detail = task.content
	print(task_detail + 'hi')
	context = {
		'task_detail': task_detail,
	}
	return render(request, 'employee_records/task_detail.html', context)

def tasks(request, pk):
	user = get_object_or_404(User, pk=pk)
	user_tasks = Task.objects.filter(assign_to_employee=pk)
	if request.user.is_authenticated:
		context = {'user_tasks': user_tasks}
	else:
		context = {'error_message':'You do not have the required permissions to view this content'}
	
	return render(request, 'employee_records/tasks.html', context)
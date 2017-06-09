from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import generic

from .models import Task

# Create your views here.
def index(request):
	# return HttpResponse('Hello there')
	return render(request, 'employee_records/base1.html')

class LoginView():
	# next = '/'
	extra_context = {'greetings': 'Hello',}

# class TaskListView(generic.ListView):
# 	model = Task
# 	template_name = 'employee_records/tasks.html'

# 	def get_context_data(self, **kwargs):
# 		user_tasks = Task.objects.filter(assign_to_employee=request.user['username'])
# 		context['user_tasks'] = user_tasks
# 		return context

def user_tasks(request, pk):
	user = get_object_or_404(User, pk=pk)
	user_tasks = Task.objects.filter(assign_to_employee=pk)
	if request.user.is_authenticated:
		context = {'user_tasks': user_tasks}
	else:
		context = {'error_message':'You do not have the required permissions to view this content'}
	
	return render(request, 'employee_records/tasks.html', context)
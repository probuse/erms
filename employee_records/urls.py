from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views


app_name = 'employee_records'

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^login/$', auth_views.login, name='login'),
	url(r'^logout/$', auth_views.logout, {'next_page': 'employee_records:login'}, name='logout'),
	url(r'^new_tasks/$', views.new_tasks, name='new_tasks'),
	url(r'^new_tasks/(?P<task_id>[0-9]+)/$', views.task_detail, name='task_detail'),
	
]
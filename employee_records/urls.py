from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^tasks/(?P<pk>[0-9]+)/$', views.user_tasks, name='tasks'),
	url(r'^login/$', auth_views.LoginView.as_view(), name='login'),
]
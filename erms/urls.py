from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
	url(r'^accounts/', include('registration.backends.default.urls')),
	url(r'^employee_records/', include('employee_records.urls')),
    url(r'^admin/', admin.site.urls),
    
]

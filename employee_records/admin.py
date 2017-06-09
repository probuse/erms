from django.db import models
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from suit_redactor.widgets import RedactorWidget

from .models import Task, Employee


admin.site.site_header = 'erms admin'
admin.site_name = 'erms'
admin.site.site_title = 'erms site admin'

class EmployeeInline(admin.StackedInline):
	model = Employee
	can_delete = False
	verbose_plural_name = 'employee'

	# fieldsets = (
	#   ('Add User As Employee', {
	# 		'fields': ('group', 'salary',)
	# 		}),
	# )

# Define a new User admin
class UserAdmin(BaseUserAdmin):
	inlines = (EmployeeInline, )

class TaskAdmin(admin.ModelAdmin):
	list_display = ('title', 'status',)
	search_fields = ('content', 'title', )
	# date_hierarchy = 'pub_date'
	list_filter = ('status', 'pub_date')
	radio_fields = {'status': admin.HORIZONTAL}
	formfield_overrides = {
		models.TextField: {'widget': RedactorWidget(editor_options={'lang': 'en'})},
	}
	
	fieldsets = (
	  (None, {
			'fields': ('title', 'content',)
			}),
		(None, {
			'fields': (('assign_to_employee', 'assign_to_group'),)
			}),
		(None, {
			'fields': ('status',)
			}),
	  (None, {
			'fields': (('pub_date', 'due_date'),)
			}),
		)
	# inlines = [
	# 	TaskInline,
	# ]

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(Employee)
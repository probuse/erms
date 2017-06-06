from django.db import models
from django.contrib import admin
from .models import Task, Employee


admin.site.site_header = 'erms admin'
admin.site.site_title = 'erms site admin'
# class TaskInline(admin.TabularInline):
# 	model = Task
# 	fk_name = 'assign_to_employee'


class TaskAdmin(admin.ModelAdmin):
	list_display = ('title', 'status', 'assign_to_employee',)
	search_fields = ('status', 'title', )
	date_hierarchy = 'pub_date'
	
	# formfield_overrides = {
	# 	models.TextField: {'widget': RichTextEditorWidget},
	# }
	
	fieldsets = (
	  (None, {
			'fields': (('title', 'content'),)
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

admin.site.register(Task, TaskAdmin)
# admin.site.register(Employee)
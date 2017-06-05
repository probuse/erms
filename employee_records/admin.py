from django.contrib import admin
from .models import Task, Employee


admin.site.site_header = 'erms admin'
admin.site.site_title = 'erms site admin'
# class TaskInline(admin.TabularInline):
# 	model = Task
# 	fk_name = 'assign_to_employee'


# class TaskAdmin(admin.ModelAdmin):
# 	inlines = [
# 		TaskInline,
# 	]

admin.site.register(Task)
admin.site.register(Employee)
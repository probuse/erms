from django.contrib.auth.models import User, Group
from django.db import models


TASK_STATUS = (
	('n', 'new'),
	('o', 'ongoing'),
	('c', 'completed')
)

class Employee(models.Model):
	user = models.OneToOneField(
		User,
		verbose_name='Employee Name', 
		on_delete=models.CASCADE
	)
	department = models.ForeignKey(Group, max_length=100)

	def __str__(self):
		return self.user.username

class Task(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()
	pub_date = models.DateField(verbose_name='Assigned on:')
	due_date = models.DateField(verbose_name='Due Date')
	assign_to_employee = models.ForeignKey(
		Employee, 
		#default='employee',
		on_delete=models.CASCADE
	)
	assign_to_group = models.ForeignKey(
		Group,
		on_delete=models.CASCADE,
		blank=True,
		null=True
	)
	status = models.CharField(max_length=1, choices=TASK_STATUS)

	def __str__(self):
		return self.title
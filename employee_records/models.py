from django.contrib.auth.models import User, Group
from django.db import models


TASK_STATUS = (
	('n', 'New'),
	('o', 'Ongoing'),
	('c', 'Completed')
)

class Employee(models.Model):
	user = models.OneToOneField(
		User,
		verbose_name='Employee Name', 
		on_delete=models.CASCADE
	)
	department = models.CharField(max_length=100)

	class Meta:
		pass

class Task(models.Model):
	title = models.CharField(max_length=100)
	assigned_task = models.TextField()
	pub_date = models.DateField()
	assign_to_employee = models.ForeignKey(
		Employee, 
		#default='employee',
		on_delete=models.CASCADE
	)
	assign_to_group = models.ForeignKey(
		Group,
		on_delete=models.CASCADE
	)
	status = models.CharField(max_length=1, choices=TASK_STATUS)

	def __str__(self):
		return self.title
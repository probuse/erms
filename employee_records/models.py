from django.db import models

TASK_STATUS = (
	('n', 'New'),
	('o', 'Ongoing'),
	('c', 'Completed')
)

class Task(models.Model):
	title = models.CharField(max_length=100)
	assigned_task = models.TextField()
	pub_date = models.DateField()
	status = models.CharField(max_length=1, choices=TASK_STATUS)

	def __str__(self):
		return self.title
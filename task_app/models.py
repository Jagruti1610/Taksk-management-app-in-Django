from django.db import models
from django.conf import settings
import datetime
from django.core.exceptions import ValidationError


# Create your models here.
class Task(models.Model):
	STATUSES = (
		(u'P', u'Pending'),
		(u'E', u'Expected'),
		(u'F', u'Finished'),
	)
	user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
	task_date = models.DateField(auto_now = True)	
	task_start_time = models.TimeField(auto_now=True)
	task_end_time = models.TimeField()
	details = models.CharField(max_length=254)
	status = models.CharField(max_length=2, choices=STATUSES, default=STATUSES[0][0])

	def clean_task_end_time(self):
		end_time = self.cleaned_data['task_end_time']
		if end_time <  datetime.datetime.now():
			raise ValidationError("The time cannot be in the past!")
		return end_time


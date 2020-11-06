from django import forms
from task_app.models import (Task)
import datetime


class TimeInput(forms.DateTimeInput):
    input_type = 'time'

class CreateTaskForm(forms.ModelForm):
	class Meta:
		model = Task
		fields = ['task_end_time', 'details', 'status']
		widgets = {
            'task_end_time':TimeInput(),
        }

	
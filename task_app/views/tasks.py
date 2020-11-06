from django.shortcuts import render, redirect, HttpResponseRedirect, reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, ListView, UpdateView, FormView
from task_app.forms import CreateTaskForm
from ..models import Task

def indexView(request):
	return render(request, 'task_app/index.html')

@login_required
def dashboardView(request):
	current_user = request.user
	tasks = Task.objects.all().filter(user_id=current_user.id)
	return render(request, 'task_app/dashboard.html', {'tasks': tasks})

def registerView(request):
	if request.method == "POST":
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('login_url')  # defined in settings.py 
	else:
		form = UserCreationForm()
	return render(request, 'registration/register.html', {'form':form})


class CreateTaskView(CreateView):
    model = Task
    form_class = CreateTaskForm
    template_name = "task_app/createViewTasks.html"

    class Meta:
        fields = ('task_start_time', 'task_end_time', 'details', 'status')

    def form_valid(self, form):
    	task_data = form.save(commit=False)
    	task_data.user = self.request.user
    	task_data.save()
    	return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):  
    	return reverse("dashboard")	
from django.urls import path
from .views import tasks
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
	path('', tasks.indexView, name='home'),
	path('dashboard/', tasks.dashboardView, name='dashboard'),
	path('login/', LoginView.as_view(), name='login_url'),
	path('register/', tasks.registerView, name='register_url'),
	path('logout/', LogoutView.as_view(), name='logout'),
	path('create_task/', tasks.CreateTaskView.as_view(), name="create_task"),
	path('<pk>/update_task', tasks.UpdateTaskView.as_view(), name="update_task"),
	path('<pk>/delete_task', tasks.DeleteTaskView.as_view(), name="delete_task"),
]
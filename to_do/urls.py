from django.urls import path

from to_do.views import index, toggle_task_status, delete_task, AddTaskView

urlpatterns = [
    path("", index, name="index"),
    path('toggle/<int:task_id>/', toggle_task_status, name='toggle_task_status'),
    path('delete/<int:task_id>/', delete_task, name='delete_task'),
    # Add URL pattern for adding a new task if needed
    path('add/', AddTaskView.as_view(), name='add_task'),
]

from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView

from to_do.forms import TaskForm
from to_do.models import Task


def index(request):
    tasks = Task.objects.order_by('is_done', '-created_datetime')
    return render(request, "index.html", {"tasks": tasks})


def toggle_task_status(request, task_id):
    task = Task.objects.get(pk=task_id)
    task.is_done = not task.is_done
    task.save()
    return redirect('index')


def delete_task(request, task_id):
    task = Task.objects.get(pk=task_id)
    task.delete()
    return redirect('index')


class AddTaskView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'add_task.html'
    success_url = reverse_lazy('index')
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from to_do.forms import TaskForm, TagForm
from to_do.models import Task, Tag


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


class TaskAddView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'task_form.html'
    success_url = reverse_lazy('index')


class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'task_form.html'
    success_url = reverse_lazy('index')


class TagListView(ListView):
    model = Tag
    template_name = 'tag_list.html'
    context_object_name = 'tags'


class TagCreateView(CreateView):
    model = Tag
    template_name = "tag_form.html"
    form_class = TagForm
    success_url = reverse_lazy('tag_list')


class TagUpdateView(UpdateView):
    model = Tag
    form_class = TagForm
    template_name = 'tag_form.html'
    success_url = reverse_lazy('tag_list')


def delete_tag(request, pk):
    task = Tag.objects.get(pk=pk)
    task.delete()
    return redirect('tag_list')

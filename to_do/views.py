from django.shortcuts import render

# Create your views here.
from to_do.models import Task


def index(request):
    tasks = Task.objects.all()
    return render(request, "index.html",{"task": tasks})
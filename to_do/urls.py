from django.urls import path

from to_do.views import index

urlpatterns = [
    path("", index, name="index"),
]
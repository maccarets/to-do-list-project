from django.urls import path

from to_do.views import (index, toggle_task_status, delete_task, TaskAddView, TagListView, TagCreateView, TagUpdateView,
                         delete_tag, TaskUpdateView)

urlpatterns = [
    path("", index, name="index"),
    path('toggle/<int:task_id>/', toggle_task_status, name='toggle_task_status'),
    path('delete/<int:task_id>/', delete_task, name='delete_task'),
    path('update/<int:pk>/', TaskUpdateView.as_view(), name='update_task'),
    path('add/', TaskAddView.as_view(), name='add_task'),
    path('tags/', TagListView.as_view(), name='tag_list'),
    path("tags/add", TagCreateView.as_view(), name="add_tag"),
    path('tags/<int:pk>/update/', TagUpdateView.as_view(), name='update_tag'),
    path('tags/<int:pk>/delete/', delete_tag, name='delete_tag'),
]

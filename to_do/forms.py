from django import forms

from to_do.models import Task, Tag


class TaskForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(), widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Task
        fields = ['content', 'deadline_datetime', 'tags']
        widgets = {
            'deadline_datetime': forms.DateTimeInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
        }


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name']
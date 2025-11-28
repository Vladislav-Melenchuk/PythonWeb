from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'time', 'category']
        widgets = {
            'time': forms.TimeInput(format='%H:%M', attrs={'type': 'time'}),
        }

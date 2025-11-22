from django import forms
from .models import Task
from django.forms import DateTimeInput

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'end_date']
        widgets = {
            'end_date': DateTimeInput(attrs={'type': 'datetime-local'})
        }

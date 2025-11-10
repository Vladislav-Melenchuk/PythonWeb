from django import forms
from .models import Event, Participant
from django.forms import inlineformset_factory

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'date']
        widgets = {
            'date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

ParticipantFormSet = inlineformset_factory(
    Event,
    Participant,
    fields=('email',),
    extra=1,
    can_delete=True
)

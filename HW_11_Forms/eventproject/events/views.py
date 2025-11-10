from django.shortcuts import render, redirect, get_object_or_404
from .models import Event
from .forms import EventForm, ParticipantFormSet

def create_event(request):
    if request.method == 'POST':
        event_form = EventForm(request.POST)
        formset = ParticipantFormSet(request.POST)
        if event_form.is_valid() and formset.is_valid():
            event = event_form.save()
            participants = formset.save(commit=False)
            for p in participants:
                p.event = event
                p.save()
            return redirect('event_detail', event_id=event.id)
    else:
        event_form = EventForm()
        formset = ParticipantFormSet()
    return render(request, 'create.html', {
        'event_form': event_form,
        'formset': formset
    })


def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    return render(request, 'detail.html', {'event': event})

def event_list(request):
    events = Event.objects.all().order_by('-date')
    return render(request, 'event_list.html', {'events': events})

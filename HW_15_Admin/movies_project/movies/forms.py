from django import forms
from .models import Movie, Review

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'description', 'release_date', 'country', 'poster', 'rating']
        widgets = {
            'release_date': forms.DateInput(format='%d.%m.%Y', attrs={'type': 'date'})
        }

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['text']
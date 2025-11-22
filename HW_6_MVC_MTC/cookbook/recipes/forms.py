from django import forms

class RecipeForm(forms.Form):
    title = forms.CharField(label="Назва", max_length=200)
    description = forms.CharField(label="Опис", widget=forms.Textarea)
    ingredients = forms.CharField(
        label="Інгредієнти",
        widget=forms.Textarea,
        help_text="Кожен інгредієнт з нового рядка"
    )
    instructions = forms.CharField(label="Інструкція", widget=forms.Textarea)

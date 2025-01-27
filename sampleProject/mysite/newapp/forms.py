from .models import Movies
from django import forms

class MovieForm(forms.ModelForm):
    class Meta:
        model=Movies
        fields = ("name","rating")


from django import forms
from django.forms import fields
from .models import City

class CityForm (forms.ModelForm):
    name = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'Enter a city'}))
    # name i kaldırmak için yazdık
    class Meta:
        model= City
        fields=("name", )
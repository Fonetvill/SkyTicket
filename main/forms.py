from django import forms
from .models import Cities

class SearchFlightsForm(forms.Form):
    from_city = forms.ModelChoiceField(
        queryset=Cities.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        label="Город отправления"
    )
    to_city = forms.ModelChoiceField(
        queryset=Cities.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        label="Город назначения"
    )
    depart_date = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        label="Дата отправления"
    )
    passengers = forms.IntegerField(
        min_value=1,
        widget=forms.NumberInput(attrs={'class': 'form-control'}),
        label="Количество пассажиров"
    )

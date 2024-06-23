from django import forms
from .models import Passengers, Gender


class PassengerRegistrationForm(forms.ModelForm):
    genderid = forms.ModelChoiceField(
        queryset=Gender.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        empty_label="Выберите пол"
    )

    class Meta:
        model = Passengers
        fields = ['firstname', 'lastname', 'dateofbirth', 'passportnumber', 'genderid', 'email']
        widgets = {
            'firstname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Имя'}),
            'lastname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Фамилия'}),
            'dateofbirth': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Дата рождения', 'type': 'date'}),
            'passportnumber': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Номер паспорта'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Электронная почта'}),
        }
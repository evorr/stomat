import datetime
from django import forms
from .models import Doctor, AppointmentSlot


class FormDoctor(forms.Form):
    doctor = forms.ModelChoiceField(queryset=Doctor.objects.all(), widget=forms.Select)


class FormText(forms.Form):
    name = forms.CharField(label="Имя", max_length=150,widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Имя'}))
    phone = forms.CharField(label="Телефон", max_length=150,
                           widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Телефон'}))
from django import forms
from .models import Mahasiswa


class FormMhs(forms.ModelForm):
    class Meta:
        model = Mahasiswa
        fields = ('nama', 'nim', 'email')
        labels = {
            'nama':'',
            'nim':'',
            'email':'',
        }
        widgets = {
            'nama': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nama'}),
            'nim': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'NIM'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
        }

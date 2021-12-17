from django import forms
from .models import DataEnkp


class EnkpForm(forms.ModelForm):
    class Meta:
        model = DataEnkp
        fields = ('plainteks', 'kunci')
        labels = {
            'plainteks': '',
            'kunci': '',
        }
        widgets = {
            'plainteks': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Plainteks'}),
            'kunci': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Kunci'}),
        }

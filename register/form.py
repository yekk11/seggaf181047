from django import forms


class ContactForm(forms.Form):
    nama = forms.CharField()
    nim = forms.CharField()
    #foto =forms.ImageField()

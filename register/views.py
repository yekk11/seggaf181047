from django.shortcuts import render
from django.http import HttpResponse
from .form import ContactForm
from .models import ContactModel

def home(request):
    contact_model = ContactModel.objects.all()
    context = {
        'contributor': 'Yekk Seggaf',
        'contact_form': contact_model
    }
    return render(request, 'register.html', context)

def create(request):
    contact_form = ContactForm()
    context = {
        'contributor': 'Yekk Seggaf',
        'contact_form': contact_form
    }
    if request.method == 'POST':
        context['nama'] = request.POST['nama']
        context['nim'] = request.POST['nim']
    return render(request, 'create.html', context)


def signin(request):
    return HttpResponse(
        '<marquee>Copyright 2021 Matematika FMIPA</marquee>'
        '<h1>Sign in Page</h1>'
    )

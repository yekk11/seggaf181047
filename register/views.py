from django.shortcuts import render
from django.http import HttpResponse
from .form import ContactForm

def home(request):
    return render(request, 'register.html')

def create(request):
    contact_form = ContactForm()
    context = {
        'judul':'Python Web | Masukkan Data',
        'contributor': 'Yekk Seggaf',
        'contact_form': contact_form
    }
    if request.method == 'POST':
        context['nama'] = request.POST['nama']
        context['nim'] = request.POST['nim']
    return render(request, 'main/create.html', context)


def signin(request):
    return HttpResponse(
        '<marquee>Copyright 2021 Matematika FMIPA</marquee>'
        '<h1>Sign in Page</h1>'
    )

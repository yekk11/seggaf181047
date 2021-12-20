from django.shortcuts import render, redirect
from django.contrib import messages


def home(request):
    return render(request, 'home.html', {})


def vcenkripsi(request):
    if request.method == 'POST':
        plaintext = request.POST['plainteks']
        key = request.POST['kunci']
        key_length = len(key)
        key_as_int = [ord(i) for i in key]
        plaintext_int = [ord(i) for i in plaintext.upper()]
        ciphertext = ''
        for i in range(len(plaintext_int)):
            value = (plaintext_int[i] + key_as_int[i % key_length]) % 26
            ciphertext += chr(value + 65)
        context = {
            'plainteks': plaintext,
            'kunci': key,
            'dispcipher': ciphertext,
        }
        return render(request, 'vcenkripsi.html', context)
    else:
        return render(request, 'vcenkripsi.html', {})


def vcdekripsi(request):
    if request.method == 'POST':
        plaintext = request.POST['cipherteks']
        key = request.POST['kunci']
        key_length = len(key)
        key_as_int = [ord(i) for i in key]
        plaintext_int = [ord(i) for i in plaintext.upper()]
        ciphertext = ''
        for i in range(len(plaintext_int)):
            value = (plaintext_int[i] - key_as_int[i % key_length]) % 26
            ciphertext += chr(value + 65)
        context = {
            'cipherteks': plaintext,
            'kunci': key,
            'dispcipher': ciphertext,
        }
        return render(request, 'vcdekripsi.html', context)
    else:
        return render(request, 'vcdekripsi.html', {})


def caesarenc(request):
    if request.method == 'POST':
        plaintext = request.POST['plainteks']
        key = request.POST['kunci']
        ciphertext = ''
        for i in range(len(plaintext)):
            special = plaintext[i]
            new_special = special.lower()
            if new_special == " ":
                ciphertext = ciphertext + ' '
            elif special.isalpha():
                ciphertext = ciphertext + chr((ord(new_special) + int(key) - 97) % 26 + 97)
        context = {
            'plainteks': plaintext,
            'kunci': key,
            'dispcipher': ciphertext,
        }
        return render(request, 'caesarenc.html', context)
    else:
        return render(request, 'caesarenc.html', {})


def caesardec(request):
    if request.method == 'POST':
        ciphertext = request.POST['cipherteks']
        key = request.POST['kunci']
        plaintext = ''
        for i in range(len(ciphertext)):
            special = ciphertext[i]
            new_special = special.lower()
            if new_special == " ":
                plaintext += ' '
            elif special.isalpha():
                plaintext += chr((ord(new_special) - int(key) - 97) % 26 + 97)
        context = {
            'cipherteks': ciphertext,
            'kunci': key,
            'dispcipher': plaintext,
        }
        return render(request, 'caesardec.html', context)
    else:
        return render(request, 'caesardec.html', {})

def lsbembed(request):
    if request.method == 'POST':
        return render(request, 'lsbembed.html', {})
    else:
        return render(request, 'lsbembed.html', {})

def lsbextract(request):
    if request.method == 'POST':
        return render(request, 'lsbextract.html', {})
    else:
        return render(request, 'lsbextract.html', {})

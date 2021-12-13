from django.shortcuts import render, redirect
from django.contrib import messages
from .form import FormMhs
from .models import Mahasiswa

def home(request):
    data_mhs = Mahasiswa.objects.all
    context = {
        'contributor': 'Yekk Seggaf',
        'data': data_mhs
    }
    return render(request, 'main/home.html', context)
def aboutme(request):
    return render(request, 'main/aboutme.html', {})

def create(request):
    if request.method == 'POST':
        form = FormMhs(request.POST or None)
        if form.is_valid():
            form.save()
        else:
            nim=request.POST['nim']
            nama=request.POST['nama']
            email=request.POST['email']
            messages.success(request, ('Error!'))
            return render(request, 'main/create.html', {
                'nim':nim,
                'nama':nama,
                'email':email,
            })
        messages.success(request, ('Data telah berhasil dimasukkan.'))
        return redirect('/')
    else:
        return render(request, 'main/create.html', {'judul':'Processing Form | Python Web'})

def del_mhs(request,del_id):
    mhsw = Mahasiswa.objects.get(pk=del_id)
    mhsw.delete()
    messages.success(request, ('Data telah dihapus.'))
    return redirect('/')

def updt_mhs(request, up_id):
    mhsw = Mahasiswa.objects.get(pk=up_id)
    form = FormMhs(request.POST or None, instance=mhsw)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'main/updt_mhs.html', {'mahasiswa': mhsw, 'form':form})
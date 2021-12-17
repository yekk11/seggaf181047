from django.shortcuts import render, redirect
from django.contrib import messages
from .form import FormMhs
from .models import Mahasiswa


def home(request):
    context = {
        'judul' : 'Halaman Utama',
        'contributor': 'Yekk Seggaf',
    }
    return render(request, 'main/home.html', context)


def aboutme(request):
    return render(request, 'main/aboutme.html', {'judul' : 'Tentang Saya'})


def data_mhs(request):
    thedata = Mahasiswa.objects.all
    return render(request, 'main/data_mhs.html', {'data': thedata,
                                                  'judul': 'List Data Mahasiswa'})


def create(request):
    if request.method == 'POST':
        form = FormMhs(request.POST or None)
        if form.is_valid():
            form.save()
        else:
            nim = request.POST['nim']
            nama = request.POST['nama']
            email = request.POST['email']
            messages.success(request, ('Error!'))
            return render(request, 'main/create.html', {
                'nim': nim,
                'nama': nama,
                'email': email,
            })
        messages.success(request, ('Data telah berhasil dimasukkan.'))
        return redirect('/data_mhs')
    else:
        return render(request, 'main/create.html', {'judul': 'Input Data Mahasiswa'})


def del_mhs(request, del_id):
    mhsw = Mahasiswa.objects.get(pk=del_id)
    mhsw.delete()
    messages.success(request, ('Data telah dihapus.'))
    return redirect('/data_mhs')


def updt_mhs(request, up_id):
    mhsw = Mahasiswa.objects.get(pk=up_id)
    form = FormMhs(request.POST or None, instance=mhsw)
    if form.is_valid():
        form.save()
        return redirect('/data_mhs')
    return render(request, 'main/updt_mhs.html', {'mahasiswa': mhsw, 'form': form})

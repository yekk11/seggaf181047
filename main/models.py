from django.db import models


class Mahasiswa(models.Model):
    nama = models.CharField(max_length=50)
    nim = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return self.nim
from django.db import models


class DataEnkp(models.Model):
    plainteks = models.CharField(max_length=100)
    kunci = models.EmailField(max_length=100)

from django.db import models

# Create your models here.


class Problem(models.Model):
    pname = models.CharField(max_length=50)
    pfrequency = models.IntegerField(default=0)


class Option(models.Model):
    oname = models.CharField(max_length=20)
    ofrequency = models.IntegerField(default=0)
    opro = models.ForeignKey('Problem', on_delete=models.CASCADE)

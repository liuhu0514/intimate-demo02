from django.db import models

# Create your models here.


class Problem(models.Model):
    pname = models.CharField(max_length=50)
    pfrequency = models.IntegerField(default=0)

    def __str__(self):
        return self.pname

    def name(self):
        return self.pname
    name.short_description = '问题'

    def frequency(self):
        return self.pfrequency
    frequency.short_description = '参与次数'


class Option(models.Model):
    oname = models.CharField(max_length=20)
    ofrequency = models.IntegerField(default=0)
    opro = models.ForeignKey('Problem', on_delete=models.CASCADE)

    def __str__(self):
        return self.oname

    def name(self):
        return self.oname
    name.short_description = '选项'

    def frequency(self):
        return self.ofrequency
    frequency.short_description = '票数'

    def pro(self):
        return self.opro
    pro.short_description = '问题'

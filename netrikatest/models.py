from django.db import models

class City(models.Model):
    cityname = models.CharField(max_length=100)

class People(models.Model):
    fio = models.CharField(max_length=200)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

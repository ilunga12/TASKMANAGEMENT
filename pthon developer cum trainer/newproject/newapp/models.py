from django.db import models
from django.db.models import Model


# Create your models here.
class task(models.Model):
    Title = models.CharField(max_length=100)
    Descrption = models.TextField(max_length=100)
    DueDate = models.DateField(max_length=100)
    Priority = models.IntegerField(default=0)


class details(models.Model):
    details=models.TextField(max_length=100)


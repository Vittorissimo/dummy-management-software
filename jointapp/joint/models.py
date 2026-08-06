from django.db import models

# Create your models here.
class Joint(models.Model):
    name = models.CharField(max_length=20)
    degree = models.IntegerField()
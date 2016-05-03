from django.db import models

class Provider(models.Model):
	Name = models.CharField(max_length=128, unique=True)
	Email = models.EmailField(max_length=70,blank=True)
	Phone_Number = models.IntegerField(default=0)
	Language = models.CharField(max_length=25,blank=True)
	Currency = models.DecimalField(max_digits=6, decimal_places=2)
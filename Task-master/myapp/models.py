from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class profile(models.Model):
	name = models.CharField(max_length=100)
	email = models.EmailField(max_length=50)
	address = models.TextField()
	phone_number = PhoneNumberField(blank=True)
	skills = models.CharField(max_length=250)
	resume =  models.FileField(upload_to ='img/',default=0,null = True, blank = True)


	def __str__(self):
		return self.name
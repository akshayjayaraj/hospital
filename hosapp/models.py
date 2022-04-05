from django.db import models

# Create your models here.
class patient_tb(models.Model):
	
	Name= models.CharField(max_length=200)
	email= models.CharField(max_length=200)
	location= models.CharField(max_length=200)
	number =models.CharField(max_length=200)
	time=models.CharField(max_length=200)
	about=models.CharField(max_length=200)
	password1=models.CharField(max_length=200)



class Doctors_tb(models.Model):
	dname=models.CharField(max_length=200)
	specailised=models.CharField(max_length=200)
	available=models.CharField(max_length=200)
	password=models.CharField(max_length=200)
	Email=models.CharField(max_length=200)

		




class token_tb(models.Model):

	time=models.CharField(max_length=200)
	date=models.CharField(max_length=200)
	problems=models.CharField(max_length=200)
	pid =models.ForeignKey(patient_tb, on_delete=models.CASCADE)	
	drid =models.ForeignKey(Doctors_tb, on_delete=models.CASCADE)	
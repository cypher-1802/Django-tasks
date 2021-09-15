from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Registration(models.Model):
	username = models.CharField(max_length=30, null=True)
	first_name = models.CharField(max_length=30,null=True)
	last_name = models.CharField(max_length=30,null=True)
	email = models.EmailField(max_length=30, null=True)
	contact = models.IntegerField(null=True)
	gender = models.CharField(max_length=10,null=True)
	passwd = models.CharField(max_length=30,null=True)
	conf_passwd = models.CharField(max_length=30,null=True)

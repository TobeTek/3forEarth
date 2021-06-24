from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager
# Create your models here.

class CustomUser(AbstractUser):
	username = models.CharField(unique=False,max_length=200)
	is_sponsor = models.BooleanField(default = False)
	is_company = models.BooleanField(default= False)
	first_name = models.CharField(max_length =200)
	last_name = models.CharField(max_length=200)
	email = models.EmailField(unique=True)
	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = []

	objects = CustomUserManager()

	def __str__(self):
		return f"{self.username} {self.email}"



	
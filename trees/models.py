from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

def get_user_type():
	user = get_user_model()

class TreeType(models.Model):
	tree_picture = models.ImageField(upload_to= 'images/',blank=True,default='no-image-icon-7.gif')
	flower_picture = models.ImageField(upload_to = 'images/',blank=True, default='no-image-icon-7.gif')
	common_name = models.CharField(max_length=100)
	latin_name = models.CharField(max_length=200)
	max_height = models.PositiveIntegerField(blank=True, null=True)
	max_age = models.PositiveIntegerField(blank =True, null = True)
	company = models.ForeignKey(get_user_model(), on_delete= models.CASCADE, related_name='tree_types')	
	price = models.FloatField()

	def __str__(self):
		return self.common_name

class Tree(models.Model):
	tree_type = models.ForeignKey(TreeType, on_delete= models.CASCADE, related_name='trees')
	date_created = models.DateTimeField(auto_now_add = True)
	date_planted = models.DateTimeField(blank=True,null=True)
	height = models.PositiveIntegerField(default=0)
	in_flower = models.BooleanField(default=False)
	latitude = models.FloatField(blank=True,null=True)
	longtitude = models.FloatField(blank=True,null=True)
	sponsor = models.ForeignKey(get_user_model(), on_delete= models.CASCADE)
	planted = models.BooleanField(default= False)


	def __str__(self):
		return f"{self.tree_type} sponsored by {self.sponsor}"
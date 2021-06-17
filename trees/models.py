from django.db import models

# Create your models here.
class TreeType(models.Model):
	tree_picture = models.ImageField(upload_to= 'images/')
	flower_picture = models.ImageField(upload_to = 'images/')
	common_name = models.CharField(max_length=100)
	latin_name = models.CharField(max_length=200)
	max_height = models.PositiveIntegerField()
	max_age = models.PositiveIntegerField(blank =True, null = True)
	company = models.CharField(max_length=255)	
	def __str__(self):
		return self.common_name

class Tree(models.Model):
	tree_type = models.ForeignKey(TreeType, on_delete= models.CASCADE, related_name='trees')
	age = models.PositiveIntegerField()
	height = models.PositiveIntegerField()
	in_flower = models.BooleanField(default= False)
	latitude = models.FloatField()
	longtitude = models.FloatField()
	sponsor = models.CharField(max_length=200)


	def __str__(self):
		return f"{self.tree_type} sponsored by {self.sponsor}"
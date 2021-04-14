from django.db import models
from django.urls import reverse

# Create your models here.
class Product(models.Model):
	
	name 		= models.CharField(max_length = 120)
	description = models.TextField(blank = True, null = True)
	price 		= models.FloatField()
	brand		= models.TextField(blank = True, null = True)
	inventory	= models.BooleanField(default = False)
	image 		= models.ImageField(upload_to='products/', blank = True, null = True)

	def get_absolute_url(self):
		return reverse("products:product-detail", kwargs = {"id": self.id})


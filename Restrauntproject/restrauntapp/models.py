from django.db import models

class FoodDetails(models.Model):
	foodname = models.CharField(max_length=50)
	price = models.PositiveIntegerField("Price")
	citi = models.CharField(max_length=50)
	flavor = models.CharField(max_length=50)

	



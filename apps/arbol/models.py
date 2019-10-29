from django.db import models

# Create your models here.

class Tree(models.Model):
	quantity = models.IntegerField()

	def __str__(self):
		return self.quantity
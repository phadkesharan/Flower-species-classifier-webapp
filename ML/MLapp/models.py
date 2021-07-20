from django.db import models

# Create your models here.

class FlowerFeatures(models.Model):

    id = models.AutoField
    sepal_length = models.FloatField()
    petal_length = models.FloatField()
    sepal_width = models.FloatField()
    petal_width = models.FloatField()
    species = models.TextField(max_length=10, default="")

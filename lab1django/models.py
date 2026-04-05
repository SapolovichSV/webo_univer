from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=80)
    author = models.CharField(max_length=200)
    publish_date = models.DateField()
    rate = models.FloatField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(5),
        ]
    )
    bestseller = models.BooleanField(default=False)

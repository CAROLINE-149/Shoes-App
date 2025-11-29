from django.db import models

# Create your models here.
class Shoe(models.Model):
    image = models.CharField(max_length=400)
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    size = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.brand} {self.model}"


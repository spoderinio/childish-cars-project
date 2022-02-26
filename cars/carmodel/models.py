from django.db import models
from carbrand.models import CarBrand

# Create your models here.


class CarModel(models.Model):
    car_brand = models.ForeignKey(
        CarBrand, blank=True, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=60)
    created_at = models.DateField()
    deleted_at = models.DateField()

    def __str__(self):
        return self.name

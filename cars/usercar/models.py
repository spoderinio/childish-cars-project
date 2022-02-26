from django.db import models
from carbrand.models import CarBrand
from carmodel.models import CarModel

# Create your models here.


class UserCar(models.Model):
    user = models.CharField('User Name', max_length=60)
    car_brand = models.ForeignKey(
        CarBrand, blank=True, null=True, on_delete=models.CASCADE)
    car_model = models.ForeignKey(
        CarModel, blank=True, null=True, on_delete=models.CASCADE)
    first_reg = models.DateField()
    odometer = models.IntegerField()
    created_at = models.DateField()
    deleted_at = models.DateField()

    def __str__(self):
        return self.user

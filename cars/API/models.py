from django.db import models

# Create your models here.


class CarBrand(models.Model):
    name = models.CharField(max_length=60)
    created_at = models.DateField(auto_now_add=True)
    deleted_at = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name


class CarModel(models.Model):
    car_brand = models.ForeignKey(
        CarBrand, blank=True, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=60)
    created_at = models.DateField()
    deleted_at = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name


class UserCar(models.Model):
    user = models.CharField('User Name', max_length=60)
    car_brand = models.ForeignKey(
        CarBrand, blank=True, null=True, on_delete=models.CASCADE, related_query_name='name')
    car_model = models.ForeignKey(
        CarModel, blank=True, null=True, on_delete=models.CASCADE)
    first_reg = models.DateField()
    odometer = models.IntegerField()
    created_at = models.DateField()
    deleted_at = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.user

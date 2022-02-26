from django.db import models

# Create your models here.


class CarBrand(models.Model):
    name = models.CharField(max_length=60)
    created_at = models.DateField()
    deleted_at = models.DateField()

    def __str__(self):
        return self.name

from django.db import models
from django.core.validators import MinValueValidator


class Country(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'country'
        verbose_name_plural = 'countries'

    def __str__(self):
        return self.name


class Service(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    duration_days = models.IntegerField(validators=[MinValueValidator(0)])
    # image = models.ImageField(upload_to='services_images/')

    def __str__(self):
        return self.name

class ServiceImage(models.Model):
    service = models.ForeignKey(Service, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='service_images/')

    def __str__(self):
        return f"Image for {self.service.name}"

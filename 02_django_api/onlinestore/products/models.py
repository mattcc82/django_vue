from django.db import models

class Manufacturer(models.Model):
    name = models.CharField(max_length=120)
    location = models.CharField(max_length=120)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Products(models.Model):
    manufacturer = models.ForeignKey(
        Manufacturer,
        on_delete=models.CASCADE,
        related_name='products'
    )
    name = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    photo = models.ImageField(blank=True, null=True)
    price = models.FloatField()
    shipping_cost = models.FloatField()
    quantity = models.SmallIntegerField()

    class Meta:
        verbose_name = 'Products'
        verbose_name_plural = 'Products'


    def __str__(self):
        return self.name

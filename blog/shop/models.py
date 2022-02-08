from django.conf import settings
from django.db import models


COUNT_PROD = (
    ("FEW", "Small amount"),
    ("ENOUGH", "Enough good"),
    ("A_LOT", "A lot of good"),
)


class Product(models.Model):
    image = models.ImageField(blank=True, null=True)
    title = models.CharField(max_length=200)
    cost = models.IntegerField()
    text = models.CharField(max_length=500)
    status = models.CharField(
        max_length=100, choices=COUNT_PROD, default="ENOUGH"
    )


class Purchase(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name="purchases", on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        Product, related_name="purchases", on_delete=models.CASCADE
    )
    count = models.IntegerField()

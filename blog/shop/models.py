from django.conf import settings
from django.db import models


COUNT_PROD = (
    ("FEW", "Small amount"),
    ("ENOUGH", "Enough good"),
    ("A_LOT", "A lot of good"),
)


class Product(models.Model):
    title = models.CharField(max_length=200)
    cost = models.IntegerField()
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    link = models.URLField(null=True, blank=True)
    status = models.CharField(
        max_length=100, choices=COUNT_PROD, default="IN_STOCK"
    )
    external_id = models.IntegerField()

    def __str__(self):
        return f"{self.title} - {self.cost}"


class Purchase(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name="purchases", on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        Product, related_name="purchases", on_delete=models.CASCADE
    )
    count = models.IntegerField()

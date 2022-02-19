from django.conf import settings
from django.db import models


COUNT_PROD = (
    ("FEW", "Small amount"),
    ("ENOUGH", "Enough good"),
    ("A_LOT", "A lot of good"),
)


ORDER_BY_CHOICES = (
    ("cost_asc", "Cost Asc"),
    ("cost_desc", "Cost Desc"),
    ("max_count", "Max Count"),
    ("max_price", "Max Cost"),
)


class Product(models.Model):
    title = models.CharField(max_length=200)
    cost = models.IntegerField()
    cost_usd = models.DecimalField(default=0, decimal_places=2, max_digits=15)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    link = models.URLField(null=True, blank=True)
    status = models.CharField(max_length=100, choices=COUNT_PROD, default="ENOUGH")
    external_id = models.IntegerField()
    favorites = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="favorite_products"
    )

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
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)

    def __str__(self):
        return f"{self.user} - {self.product} - {self.count}"

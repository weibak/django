from django.shortcuts import render
import logging
from shop.models import Product
logger = logging.getLogger(__name__)


def product_list(request):
    products = Product.objects.all()
    logger.info(f"Products")
    return render(request, "products/product_list.html", {"products": products})

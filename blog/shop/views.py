from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
import logging
from django.db.models import Sum, F
from shop.forms import ProductFiltersForm
from shop.models import Product, Purchase

logger = logging.getLogger(__name__)


def product_list(request):
    products = Product.objects.all()
    filters_form = ProductFiltersForm(request.GET)

    if filters_form.is_valid():
        cost__gt = filters_form.cleaned_data["cost__gt"]
        if cost__gt:
            products = products.filter(cost__gt=cost__gt)

        cost__lt = filters_form.cleaned_data["cost__lt"]
        if cost__lt:
            products = products.filter(cost__lt=cost__lt)

        order_by = filters_form.cleaned_data["order_by"]
        if order_by:
            if order_by == "cost_asc":
                products = products.order_by("cost")
            if order_by == "cost_desc":
                products = products.order_by("-cost")
            if order_by == "max_count":
                products = products.annotate(total_count=Sum("purchases__count")).order_by(
                    "-total_count"
                )
            if order_by == "max_price":
                products = products.annotate(
                    total_cost=Sum("purchases__count") * F("cost")
                ).order_by("-total_cost")
    return render(request, "products/product_list.html", {"filters_form": filters_form, "products": products})


def product_view(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == "POST":
        if request.POST.get("count"):
            Purchase.objects.create(product=product, user=request.user, count=request.POST.get("count"))
            return redirect("product_card", product_id=product_id)

        if request.user.is_authenticated and request.method == "POST":

            if request.POST["action"] == "add":
                product.favorites.add(request.user)
                messages.info(request, "Product successfully added to favorites")
            elif request.POST["action"] == "remove":
                product.favorites.remove(request.user)
                messages.info(request, "Product successfully removed to favorites")
            redirect("product_card", product_id=product.id)
    return render(request, "products/details.html", {
        "product": product,
        "is_product_in_favorites": request.user in product.favorites.all(),
    })

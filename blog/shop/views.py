from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
import logging

from django.views.generic import TemplateView

from shop.forms import ProductFiltersForm
from shop.models import Product, Purchase
from shop.queries import filter_products

logger = logging.getLogger(__name__)


class ProductView(TemplateView):
    template_name = "products/product_list.html"

    def get_context_data(self, **kwargs, ):
        logger.info("test message")
        products = Product.objects.all()
        filters_form = ProductFiltersForm(self.request.GET)

        if filters_form.is_valid():
            cost__gt = filters_form.cleaned_data["cost__gt"]
            cost__lt = filters_form.cleaned_data["cost__lt"]
            order_by = filters_form.cleaned_data["order_by"]
            products = filter_products(products, cost__gt, cost__lt, order_by)

        paginator = Paginator(products, 30)
        page_number = "page"
        products = paginator.get_page(page_number)
        return {"products": products, "filters_form": filters_form}


def product_list(request):
    products = Product.objects.all()
    filters_form = ProductFiltersForm(request.GET)

    if filters_form.is_valid():
        cost__gt = filters_form.cleaned_data["cost__gt"]
        cost__lt = filters_form.cleaned_data["cost__lt"]
        order_by = filters_form.cleaned_data["order_by"]
        products = filter_products(products, cost__gt, cost__lt, order_by)

    paginator = Paginator(products, 30)
    page_number = request.GET.get("page")
    products = paginator.get_page(page_number)
    return render(
        request,
        "products/product_list.html",
        {"filters_form": filters_form, "products": products},
    )


def product_view(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == "POST":
        if request.POST.get("count"):
            Purchase.objects.create(
                product=product, user=request.user, count=request.POST.get("count")
            )
            return redirect("product_card", product_id=product_id)
        if request.user.is_authenticated and request.method == "POST":
            if request.POST["action"] == "add":
                product.favorites.add(request.user)
                messages.info(request, "Product successfully added to favorites")
            elif request.POST["action"] == "remove":
                product.favorites.remove(request.user)
                messages.info(request, "Product successfully removed to favorites")
            redirect("product_card", product_id=product.id)
    return render(
        request,
        "products/details.html",
        {
            "product": product,
            "is_product_in_favorites": request.user in product.favorites.all(),
        },
    )

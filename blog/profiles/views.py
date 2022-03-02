import logging
from django.http import HttpResponse
from django.shortcuts import render, redirect

from profiles.models import Profile
from django.contrib.auth.models import User

from shop.forms import PurchasesFiltersForm
from shop.models import Purchase
from shop.queries import filter_purchases

logger = logging.getLogger(__name__)


def profiles_index(request):
    # Processing GET params
    value = request.GET.get("get-key-1")
    value and logger.info(f"get-key-1 = {value}")
    value = request.GET.get("get-key-2")
    value and logger.info(f"get-key-2 = {value}")
    value = request.GET.get("get-key-3")
    value and logger.info(f"get-key-3 = {value}")

    # Processing POST params
    value = request.POST.get("post-key-1")
    value and logger.info(f"post-key-1 = {value}")
    value = request.POST.get("post-key-2")
    value and logger.info(f"post-key-2 = {value}")
    value = request.POST.get("post-key-3")
    value and logger.info(f"post-key-3 = {value}")

    return HttpResponse("Profiles index view")


# поиск по user
def search_profile(request):
    username = request.user
    logger.info(f"User with name = {username}")
    user = User.objects.filter(username=username).first()
    profile = Profile.objects.filter(user_id=user).first()
    name = user.first_name
    surname = user.last_name
    image = profile.image.url
    status = profile.status
    age = profile.age
    output = (
        "<h2> Name: {0}</h2><br>"
        "<h2> Surname: {1}</h2><br>"
        "<h2> Image: {2}</h2><br>"
        "<h2>Status: {3}</h2><br>"
        "<h2> Age: {4}</h2><br>".format(name, surname, image, status, age)
    )
    return HttpResponse(output)


def profile_view(request):
    if request.user.is_anonymous:
        return redirect("auth")
    profile = Profile.objects.get(user=request.user)
    purchases = Purchase.objects.filter(user=request.user).all()
    logger.info(f"Purchases of {request.user}")
    filters_form = PurchasesFiltersForm(request.GET)

    if filters_form.is_valid():
        order_by = filters_form.cleaned_data["order_by"]
        purchases = filter_purchases(purchases, order_by)

    return render(
        request,
        "profile.html", {
            "profile": profile,
            "purchases": purchases,
            "filters_form": filters_form}
    )

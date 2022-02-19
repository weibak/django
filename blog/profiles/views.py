import logging
from django.http import HttpResponse

from profiles.models import Profile
from django.contrib.auth.models import User


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
    username = request.GET.get("user", "")
    logger.info(f"User with name = {username}")
    user = User.objects.filter(username=username).first()
    profile = Profile.objects.filter(user_id=user).first()
    name = user.first_name
    surname = user.last_name
    image = profile.image
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

from django.http import HttpResponse
import logging


logger = logging.getLogger(__name__)


def blog1_index(request):
    value = request.GET.get("key_1")
    logger.info(value)
    return HttpResponse("Blog_1 index view")


def blog1_index_2(request):
    value = request.GET.get("key_1")
    logger.info(value)
    a = input('some word: ')
    return HttpResponse(f"{a}, Blog_1 index view111111111")


def post_r(request):
    if request == "POST":
        value = request("post_r_1")
        logger.info(value)
    return HttpResponse("Blog_1 index view")

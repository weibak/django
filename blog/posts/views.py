from django.http import HttpResponse
import logging


logger = logging.getLogger(__name__)


def posts_index(request):
    value = request.GET.get("key")
    logger.info(value)
    return HttpResponse("Posts index view")


def posts_index_2(request):
    value = request.GET.get("key_1")
    logger.info(value)
    return HttpResponse("Posts index view111111111")


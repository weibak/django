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
    return HttpResponse("Blog_1 index view111111111")
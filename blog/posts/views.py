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


def search_title(request):
    value = request.GET.get("title", "")
    post = request.GET.get("Title", "Post")
    logger.info(f"Post with = {value}")
    title = "<h2>Post</h2><h3>Title {0} Title: {1}</h3>".format(value, post)

    return HttpResponse(title)

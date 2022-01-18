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


# get запрос через URL
def search_title(request, post):
    value = request.GET.get("title", "")
    title = request.GET.get("title", "")
    logger.info(f"Post with title = {value}")
    output = "<h2> Title N {0}</h2><br><h2>Post {1} </h2>".format(post, title)
    return HttpResponse(output)

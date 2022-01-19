from django.http import HttpResponse
import logging
from posts.models import Post


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
def search_title(request):
    title = request.GET.get("title", "")
    logger.info(f"Post with title = {title}")
    output = f"<h2> Title: {title}</h2><br><h2> </h2>"
    return HttpResponse(output)


# поиск по slug в URL
def search_slug(request):
    slug = request.GET.get("slug", "")
    logger.info(f"Post with slug = {slug}")
    post = Post.objects.filter(slug=slug).first()
    title = post.title
    author = post.author
    image = post.image
    text = post.text
    output = "<h2> Title: {0}</h2><br>"\
             "<h2> Author: {1}</h2><br>" \
             "<h2> Image: {2}</h2><br>" \
             "<h1>Text: {3}<h1><br>".format(title, author, image, text)
    return HttpResponse(output)


# поиск по slug в URL
def search_user_posts(request):
    author = request.GET.get("author", "")
    logger.info(f"Posts with author = {author}")
    Post.objects.filter(author=request.user)
    title = Post.objects.title
    author = Post.objects.author
    text = Post.objects.text
    image = Post.objects.text
    created_at = Post.objects.created_at
    context = "<h2> Author: {0}</h2><br>" \
              "<h2> Title: {1}</h2><br>" \
              "<h2> Image: {2}</h2><br>" \
              "<h2> Text: {3}</h2><br>" \
              "<h2> Created at: {4}</h2><br>".format(author, title, image, text, created_at)

    return HttpResponse(context)

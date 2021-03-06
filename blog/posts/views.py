from django.http import HttpResponse
import logging
from django.shortcuts import redirect, render
from posts.forms import PostForm
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
    output = (
        "<h2> Title: {0}</h2><br>"
        "<h2> Author: {1}</h2><br>"
        "<h2> Image: {2}</h2><br>"
        "<h1>Text: {3}<h1><br>".format(title, author, image, text)
    )
    return HttpResponse(output)


# поиск по slug в URL
def search_user_posts(request):
    author = request.GET.get("author", "")
    logger.info(f"Posts with author = {author}")
    posts = Post.objects.filter(author__username=author)
    context = ""
    for post in posts:
        context += f"<div style='border: 1px solid black'>"
        context += f"<h2> Author: {post.author}</h2><br>"
        context += f"<h2> Title: {post.title}</h2><br>"
        context += f"<h2> Image: {post.image}</h2><br>"
        context += f"<h2> Text: {post.text}</h2><br>"
        context += f"<div> Created at: {post.created_at}</h2><br>"
        context += f"</div>"
    return HttpResponse(context)


def create_post(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = PostForm(request.POST, request.FILES)
            if form.is_valid():
                logger.info(form.cleaned_data)
                post = Post.objects.create(author=request.user, **form.cleaned_data)
                post.save()
                return redirect(
                    "/",
                )
        else:
            form = PostForm()
        return render(request, "posts/create_post.html", {"form": form})
    else:
        return redirect("auth")


def post_list(request):
    if request.user.is_anonymous:
        return redirect("auth")
    posts = Post.objects.filter(author=request.user)
    logger.info(f"Posts of {request.user}")
    return render(request, "posts/list.html", {"posts": posts})


def post_list_all(request):
    if request.user.is_anonymous:
        return redirect("auth")
    posts = Post.objects.order_by("-created_at")
    logger.info(f"Posts of all users")
    return render(request, "posts/list.html", {"posts": posts})


def post_view(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, "posts/post.html", {"post": post})

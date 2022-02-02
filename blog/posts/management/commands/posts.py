import logging

from django.core.management.base import BaseCommand

from posts.models import Post

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Posts "

    def handle(self, *args, **options):
        posts = Post.objects.all()
        for post in posts:

            logger.info(f"Post {post.id} - Title {post.title}")

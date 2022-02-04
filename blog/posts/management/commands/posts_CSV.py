import logging

from django.conf import settings
from django.core.management.base import BaseCommand

from posts.models import Post
import csv


logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Posts in CSV"

    def handle(self, *args, **options):
        with open(settings.BASE_DIR / "posts.csv", "w") as file:
            writer = csv.writer(file)
            for post in Post.objects.all():
                writer.writerow([post.id, post.title, post.slug, post.text, post.created_at, post.author])

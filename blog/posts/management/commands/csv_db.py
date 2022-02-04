import logging

from django.conf import settings
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from posts.models import Post
import csv


logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Posts in CSV"

    def handle(self, *args, **options):
        with open(settings.BASE_DIR / "posts.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                user = User.objects.filter(username=row[4]).first()
                Post.objects.create(
                    title=row[0],
                    slug=row[1],
                    text=row[2],
                    author=user
                )

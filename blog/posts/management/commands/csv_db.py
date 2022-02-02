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
                user = User.objects.create(username=row[6])
                Post.objects.create(
                    id=row[0],
                    title=row[1],
                    slug=row[3],
                    text=row[4],
                    created_at=row[4],
                    author=user
                )

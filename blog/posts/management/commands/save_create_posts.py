import csv
from pathlib import Path
import requests
from django.conf import settings
from django.contrib.auth.models import User
from django.core.management import BaseCommand

from posts.models import Post


class Command(BaseCommand):
    help = "Posts in CSV"

    def handle(self, *args, **options):
        def load_file(link, name_in_system):
            filename = Path(name_in_system)
            url = link
            response = requests.get(url)
            filename.write_bytes(response.content)

        load_file(
            "https://www.oma.by/upload/Sh/imageCache/da7/ddf/793956f6eb72f2022e353d0043b49ac8.jpg",
            "load_csv_posts_file.jpg",
        )

        with open(settings.BASE_DIR / "load_csv_posts_file.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                user = User.objects.filter(username=row[5]).first()
                Post.objects.create(author=user, title=row[1], slug=row[2], text=row[3])

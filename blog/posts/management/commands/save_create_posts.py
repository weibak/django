from pathlib import Path
import requests
from django.core.management import BaseCommand


class Command(BaseCommand):
    help = "Posts in CSV"

    def handle(self, *args, **options):
        def load_file(link, name_in_system):
            filename = Path(name_in_system)
            url = link
            response = requests.get(url)
            filename.write_bytes(response.content)

        load_file('https://github.com/weibak/lessons/blob/master/LICENSE.txt', 'load_license_file.txt')
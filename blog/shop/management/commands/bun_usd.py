import logging
from django.core.management.base import BaseCommand

from shop.tasks import run_bun_usd

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Crawl BUN_USD"

    def handle(self, *args, **options):
        run_bun_usd.delay()

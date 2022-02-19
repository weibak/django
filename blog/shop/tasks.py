import logging
from pathlib import Path

import requests
from django.conf import settings
from django.db.models import F
from django_rq import job

from shop.models import Product
from shop.spiders.oma import OmaSpider
from scrapy import signals
from scrapy.crawler import CrawlerProcess
from scrapy.signalmanager import dispatcher
from scrapy.utils.project import get_project_settings


logger = logging.getLogger(__name__)


@job
def run_products_update():
    Product.objects.filter(cost=0).update(status="FEW")


@job
def run_oma_spider():
    def crawler_results(signal, sender, item, response, spider):
        item["cost"] = int(item["cost"].split(",")[0])
        if item["image"]:
            response = requests.get(item["image"])
            if response.ok:
                path = Path(item["image"])
                open(settings.MEDIA_ROOT / path.name, "wb").write(response.content)
                item["image"] = path.name
        Product.objects.update_or_create(
            external_id=item["external_id"], defaults=item
        )

    dispatcher.connect(crawler_results, signal=signals.item_scraped)

    process = CrawlerProcess(get_project_settings())
    process.crawl(OmaSpider)
    process.start()


@job
def run_bun_usd():
    url = "https://free.currconv.com/api/v7/convert?q=USD_BYN,BYN_USD&compact=ultra&apiKey=f6265e996ab6ead1cf1c"
    response = requests.get(url)
    logger.info(response)
    data = response.json()
    logger.info(data)
    exchange = round(float(data["USD_BYN"]), 2)
    logger.info(exchange)
    Product.objects.all().update(cost_usd=F('cost')/exchange)

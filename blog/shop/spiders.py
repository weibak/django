import logging
from pathlib import Path

import scrapy
import logging
import requests

from blog import settings

logger = logging.getLogger(__name__)


class OmaSpider(scrapy.Spider):
    name = "oma.by"
    allowed_domains = ["https://www.oma.by"]
    start_urls = ["https://www.oma.by/elektroinstrument-c"]

    def __init__(self, *args, **kwargs):
        logger = logging.getLogger("scrapy")
        logger.setLevel(logging.ERROR)
        super().__init__(*args, **kwargs)

    def parse(self, response, **kwargs):
        logger.info("processing:"+response.url)
        for product in response.css(".catalog-grid .product-item"):
            external_id = int(product.css("::attr(data-ga-product-id)").get()),
            image_link = "https://oma.by/" + str(product.css('.product-item_img-box img:first-child::attr(data-lazy)').get())
            filename = Path(settings.BASE_DIR / f"{external_id}.jpg")
            responsee = requests.get(image_link)
            filename.write_bytes(responsee.content)
            if not image_link:
                external_id = int(product.css("::attr(data-ga-product-id)").get()),
                image_link = "https://oma.by/" + str(product.css('.product-item_img-box img:first-child::attr(data-src)').get())
                filename = Path(settings.BASE_DIR / f"{external_id}.jpg")
                responsee = requests.get(image_link)
                filename.write_bytes(responsee.content)
            data = {
                "external_id": f"{self.allowed_domains[0]}{external_id}",
                "title": product.css(".product-title-and-rate-block .wrapper::text").get().strip(),
                "cost": product.css(".product-price-block .price__normal::text").get().strip(),
                "link": f"{self.allowed_domains[0]}{product.css('a.area-link::attr(href)').get()}",
                "image": f"{self.allowed_domains[0]}{image_link}",
            }
            yield data

        NEXT_PAGE_SELECTOR = '.btn__nav-right::attr(href)'
        next_page = response.css(NEXT_PAGE_SELECTOR).extract_first()
        if next_page:
            logger.info({next_page})
            yield scrapy.Request(
                response.urljoin(next_page),
                callback=self.parse
                )

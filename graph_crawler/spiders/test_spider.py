from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class DemoSpider(CrawlSpider):
    name = "DemoCrawler"
    allowed_domains = ["toscrape.com"]
    start_urls = ["https://books.toscrape.com/"]

    rules = (
        Rule(LinkExtractor(allow="catalogue/category")),
    )
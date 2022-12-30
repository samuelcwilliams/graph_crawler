from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class QouteSpider(CrawlSpider):
    name = "QouteCrawler"
    allowed_domains = ["toscrape.com"]
    start_urls = ["http://quotes.toscrape.com/"]

    rules = (
        Rule(LinkExtractor(allow="/author"), callback="parse_item"),
    )

    """
    TODO: Implement function to parse responses from the QouteSpider
    """
    def parse_item(self, response):
        yield {
            "author": response.css(".author-title h3::text").get(),
            "qoute": response.css(".author-qoute h4::text").get(),
        }

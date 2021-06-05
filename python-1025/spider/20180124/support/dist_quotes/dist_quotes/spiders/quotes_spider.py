from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor
from scrapy_redis.spiders import RedisCrawlSpider


class QuotesSpider(RedisCrawlSpider):
    name = "quotes"
    redis_key = "quotes:start_urls"
    allowed_domains = ["quotes.toscrape.com"]

    rules = (
        Rule(LinkExtractor(), callback='parse_page', follow=True),
    )

    def parse_page(self, response):
        divs = response.xpath('//div[@class="quote"]')
        for div in divs:
            text = div.xpath('span[@class="text"]/text()').extract_first()
            author = div.xpath('.//small/text()').extract_first()
            tags = div.xpath('div[@class="tags"]/a/text()').extract()
            yield dict(text=text, author=author,
                       tags=tags, flag=getattr(self, 'flag', 'default'))

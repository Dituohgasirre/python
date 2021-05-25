from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor
from scrapy_redis.spiders import RedisSpider


class QuotesSpider(RedisSpider):
    name = "quotes2"
    redis_key = "quotes:start_urls"
    allowed_domains = ["quotes.toscrape.com"]

    def parse(self, response):
        divs = response.xpath('//div[@class="quote"]')
        for div in divs:
            text = div.xpath('span[@class="text"]/text()').extract_first()
            author = div.xpath('.//small/text()').extract_first()
            tags = div.xpath('div[@class="tags"]/a/text()').extract()
            yield dict(text=text, author=author,
                       tags=tags, flag=getattr(self, 'flag', 'default'))
        for a in response.css('a'):
            yield response.follow(a)

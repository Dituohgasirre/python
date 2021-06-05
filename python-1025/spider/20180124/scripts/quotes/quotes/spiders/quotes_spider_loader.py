import scrapy

from quotes.items import QuotesItem, QuotesItemLoader


class QuotesSpider(scrapy.Spider):
    name = "quotes-loader"
    allowed_domains = ['toscrape.com']

    def start_requests(self):
        urls = ['http://quotes.toscrape.com']
        for url in urls:
            yield scrapy.Request(url)

    def parse(self, response):
        divs = response.xpath('//div[@class="quote"]')
        for div in divs:
            l = QuotesItemLoader(selector=div)
            l.add_xpath('text', './/span[@class="text"]/text()')
            l.add_xpath('author', './/*[@itemprop="author"]/text()')
            l.add_xpath('tags', './/*[@itemprop="keywords"]/@content')
            item = l.load_item()
            yield item

        for a in response.css('a'):
            yield response.follow(a)

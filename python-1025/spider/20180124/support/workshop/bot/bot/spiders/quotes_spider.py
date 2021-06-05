import scrapy
import json

from bot.items import BotItem


class QuoteSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'http://localhost:8000/quotes_1.html',
        'http://localhost:8000/quotes_1.html',
        'http://localhost:8000/quotes_1.html',
        'http://localhost:8000/quotes_2.html',
        'http://localhost:8000/quotes_2.html',
        'http://localhost:8000/quotes_2.html',
    ]

    def parse(self, response):
        for div in response.xpath('//div[@class="quote"]'):
            text = div.xpath('span[@class="text"]/text()').extract_first()
            author = div.xpath('.//small/text()').extract_first()
            tags = div.xpath('.//meta/@content').extract_first()
            yield BotItem(text=text, author=author, tags=tags)

    # def parse(self, response):
    #     pagenum = response.url.split('/')[-2]
    #     filename = 'quotes_%s.html' % pagenum
    #     with open(filename, 'w') as f:
    #         f.write(response.text)

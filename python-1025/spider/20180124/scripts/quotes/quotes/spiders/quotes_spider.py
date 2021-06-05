import scrapy

from quotes.items import QuotesItem


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    allowed_domain = ['quotes.toscrape.com']

    def start_requests(self):
        urls = ['http://quotes.toscrape.com/']
        for url in urls:
            yield scrapy.Request(url)

    def parse(self, response):
        divs = response.xpath('//div[@class="quote"]')
        for div in divs:
            text = div.xpath('.//span[@class="text"]/text()').extract_first()
            author = div.xpath('.//*[@itemprop="author"]/text()').extract_first()
            tags = div.xpath('.//*[@itemprop="keywords"]/@content').extract_first()
            # record = {'text': text, 'author': author, 'tags': tags}
            item = QuotesItem()
            item['text'] = text
            item['author'] = author
            item['tags'] = tags
            yield item

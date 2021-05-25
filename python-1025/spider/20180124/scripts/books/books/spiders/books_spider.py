import scrapy

from books.items import BooksItem, BooksItemLoader


class BooksSpider(scrapy.Spider):
    name = "books"
    allowed_domain = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/']

    def parse(self, response):
        for li in response.xpath('//ol/li'):
            l = BooksItemLoader(selector=li, response=response)
            l.add_xpath('title', './/h3/a/text()')
            l.add_css('price', '.price_color::text')
            l.add_css('image_urls', 'img::attr(src)')
            yield l.load_item()

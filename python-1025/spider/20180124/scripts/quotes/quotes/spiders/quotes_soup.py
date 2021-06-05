import scrapy
from bs4 import BeautifulSoup as BS


class QuotesSpider(scrapy.Spider):
    name = "quotes-soup"
    allowed_domain = ['quotes.toscrape.com']

    def start_requests(self):
        urls = ['http://quotes.toscrape.com/']
        for url in urls:
            yield scrapy.Request(url)

    def parse(self, response):
        soup = BS(response.text, 'lxml')
        title = soup.title.string
        yield {'title': title, 'url': response.url}

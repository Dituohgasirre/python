import scrapy

from quotes.items import QuotesItem


class QuotesSpider(scrapy.Spider):
    name = "lagou"
    allowed_domain = ['lagou.com']

    def start_requests(self):
        urls = ['https://www.lagou.com/jobs/3796922.html']
        for url in urls:
            yield scrapy.Request(url)

    def parse(self, response):
        open('lagou_job.html', 'w').write(response.text)

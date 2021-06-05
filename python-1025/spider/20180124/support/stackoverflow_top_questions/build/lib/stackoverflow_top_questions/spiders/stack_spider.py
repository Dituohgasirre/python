import scrapy


class StackSpider(scrapy.Spider):
    name = 'stack'
    start_urls = ['https://stackoverflow.com/?tab=month']

    def parse(self, response):
        hrefs = response.css('a.question-hyperlink::attr(href)').extract()
        texts = response.css('a.question-hyperlink::text').extract()
        names = ('text', 'href')
        records = [dict(zip(names, item)) for item in list(zip(texts, hrefs))]
        return records

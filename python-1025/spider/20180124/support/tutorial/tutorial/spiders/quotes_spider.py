import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for quote in response.xpath('//div[@class="quote"]'):
            text = quote.xpath('span[1]/text()').extract_first()
            author = quote.xpath('.//small/text()').extract_first()
            tags = quote.xpath('div[@class="tags"]/a[@class="tag"]/text()').extract()
            yield dict(text=text, author=author, tags=tags)

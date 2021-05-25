import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = [
        'http://quotes.toscrape.com',
    ]

    def parse(self, response):
        # yield the items
        divs = response.xpath('//div[@class="quote"]')
        for div in divs:
            text = div.xpath('span[@class="text"]/text()').extract_first()
            author = div.xpath('.//small/text()').extract_first()
            tags = div.xpath('div[@class="tags"]/a/text()').extract()
            yield dict(text=text, author=author, tags=tags)

        # follow links
        for url in response.xpath('//a/@href').extract():
            url = response.urljoin(url)
            yield scrapy.Request(url=url, callback=self.parse)

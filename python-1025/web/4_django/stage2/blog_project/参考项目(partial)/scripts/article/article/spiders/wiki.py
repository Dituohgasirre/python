import scrapy


class WikiSpider(scrapy.Spider):
    name = 'wiki'
    start_urls = ['https://en.wikipedia.org/wiki/Unix']
    allowed_domains = ['en.wikipedia.org']

    def parse(self, response):
        title = response.css('h1::text').extract_first()
        content = ' '.join(response.css('#bodyContent p::text').extract())
        if title and content:
            yield {'title': title, 'content': content}

        urls = response.xpath('//a/@href').extract()
        for url in urls:
            url = response.urljoin(url)
            yield scrapy.Request(url=url, callback=self.parse)

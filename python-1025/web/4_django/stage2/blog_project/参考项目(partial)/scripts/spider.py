import re

from scrapy import Spider, Request


class TagSpider(Spider):
    name = 'tag'
    start_urls = ['http://dmoztools.net/Computers/']
    allowed_domains = ['dmoztools.net']

    def parse(self, response):
        items = response.css('#subcategories-div .cat-item')
        s = items.css('a div::text')
        pat = re.compile('^[a-zA-Z ]+$')
        tags = [x.strip() for x in s.extract()]
        tags = [x for x in tags if x and pat.match(x)]
        yield {'names': tags}

        targets = items.css('a::attr(href)').extract()
        for url in targets:
            if not url.startswith('/Computers/'):
                continue
            url = response.urljoin(url)
            yield Request(url=url, callback=self.parse)

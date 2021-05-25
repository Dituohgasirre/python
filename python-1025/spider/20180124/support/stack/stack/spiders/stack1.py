import scrapy


class StackSpider(scrapy.Spider):
    name = 'stack1'
    start_urls = [
        'https://stackoverflow.com/?tab=month',
    ]

    def parse(self, response):
        divs = response.xpath('//div[@id="qlist-wrapper"]/div[1]/div[1]/div')
        for div in divs:
            title = div.xpath('.//h3/a/text()').extract_first()
            url = div.xpath('.//h3/a/@href').extract_first()
            url = response.urljoin(url)
            tags = div.xpath('.//div[@class="summary"]/div[1]/a/text()').extract()
            item = dict(title=title, url=url, tags=tags)
            request = scrapy.Request(url=url, callback=self.parse_viewed,
                                     meta={'item': item})
            yield request

    def parse_viewed(self, response):
        item = response.request.meta['item']
        v = response.xpath('//table[@id="qinfo"]/tr[2]//b/text()').extract_first()
        item['viewed'] = v
        return item


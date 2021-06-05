import scrapy


class StackSpider(scrapy.Spider):
    name = 'stack'
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
            request = scrapy.Request(url=url,
                                     callback=self.determine_accepted,
                                     meta={'item': item})
            yield request

    def determine_accepted(self, response):
        accepted = bool(response.xpath('//span[text()="accepted"]'))
        item = response.request.meta['item']
        item['accepted'] = accepted
        return item

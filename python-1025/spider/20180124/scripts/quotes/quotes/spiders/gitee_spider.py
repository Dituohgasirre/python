import scrapy


class GiteeSpider(scrapy.Spider):
    name = 'gitee'
    start_urls = ['https://gitee.com/explore/recommend']

    def parse(self, response):
        divs = response.css('#git-discover-list .item')
        for div in divs:
            url = div.css('a.title::attr(href)').re_first('^/[^/]+')
            user_name = url[1:]
            item = {'user_name': user_name}
            url = response.urljoin(url)
            yield scrapy.Request(url, callback=self.extract_join_time, meta={'item': item})

    def extract_join_time(self, response):
        item = response.meta['item']
        item['join_time'] = response.css('span.timeago::attr(title)').re_first(r'(^.*?) \+')
        yield item

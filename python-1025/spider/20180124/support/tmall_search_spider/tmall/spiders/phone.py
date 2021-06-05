# -*- coding: utf-8 -*-
import scrapy


class PhoneSpider(scrapy.Spider):
    name = 'phone'
    allowed_domains = ['list.tmall.com']
    start_urls = ['https://list.tmall.com/search_product.htm?q=%CC%EA%D0%EB%B5%B6&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton']

    def parse(self, response):
        open('/tmp/tmall.html', 'w').write(response.text)
        next_url = response.css('a.ui-page-next::attr(href)').extract_first()
        next_url = response.urljoin(next_url)
        yield scrapy.Request(next_url, callback=self.parse2)
        """
        all_phones = response.css('#J_ItemList a.productImg img')
        current_page = response.xpath('//input[@name="jumpto"]/@value').extract_first()
        total_pages = response.xpath('//form[@name="filterPageForm"]/text()').re('共([0-9]+)页')
        next_url = response.css('a.ui-page-next::attr(href)').extract_first()
        next_url = response.urljoin(next_url)
        """

    def parse2(self, response):
        open('/tmp/tmall2.html', 'w').write(response.text)

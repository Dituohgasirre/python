# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

import requests
from scrapy import signals
from scrapy.exceptions import CloseSpider
from scrapy.http.response.html import HtmlResponse
import scrapy

from quotes.items import QuotesItem


class QuotesSpiderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class LimitItemSpiderMiddleware:

    def __init__(self, *args, **kargs):
        self.item_count = 0

    def process_spider_output(self, response, result, spider):
        for i in result:
            if self.item_count >= 2:
                raise CloseSpider('all items collected (%s)' % self.item_count)
            if isinstance(i, QuotesItem):
                self.item_count += 1
            yield i


class QuotesKillRequestSpiderMiddleware:

    def process_spider_output(self, response, result, spider):
        for i in result:
            if isinstance(i, scrapy.Request):
                continue
            yield i


class QuotesJsDownloaderMiddleware:

    def __init__(self, crawler):
        self.crawler = crawler

    def process_request(self, request, spider):
        js = request.meta.get('js')
        if js:
            url = request.url
            print('processing js request: %s' % url)
            js_api = self.crawler.settings['JS_SERVER_API']
            r = requests.post(js_api, data={'url': url})
            if r.ok:
                html_code = r.json()['text']
            return HtmlResponse(url, status=r.status_code, headers=r.headers,
                                body=html_code.encode(), request=request)

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler)

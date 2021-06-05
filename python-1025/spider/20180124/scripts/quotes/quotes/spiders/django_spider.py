import scrapy
from scrapy import FormRequest


class DjangoSpider(scrapy.Spider):
    name = 'django'
    start_urls = ['http://localhost:8000/admin/login/']
    after_login_urls = ['http://localhost:8000/admin/polls/question/']

    def parse(self, response):
        yield FormRequest.from_response(
            response,
            url=response.url,
            formdata={'username': 'admin', 'password': 'abcd/1234'},
            callback=self.after_post
        )

    def after_post(self, response):
        if 'Log in' not in response.css('title::text').extract_first():
            for url in self.after_login_urls:
                yield scrapy.Request(url, callback=self.extract_data)

    def extract_data(self, response):
        # from scrapy.shell import inspect_response, fetch
        # inspect_response(response, self)
        texts = response.css('tbody a::text').extract()
        urls = response.css('tbody a::attr(href)').extract()
        header = ['text', 'url']
        for x in zip(texts, urls):
            yield dict(zip(header, x))

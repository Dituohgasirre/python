import scrapy


class DjangoSpider(scrapy.Spider):
    name = 'django'
    start_urls = ['http://127.0.0.1:8000/admin/login/']
    after_login_urls = ['http://127.0.0.1:8000/admin/polls/question/']

    def parse(self, response):
        yield scrapy.FormRequest.from_response(
                response,
                formdata={'username': 'admin',
                          'password': 'abcd/1234'},
                callback=self.after_login,
                errback=self.errback)

    def after_login(self, response):
        if response.css('form#login-form'):
            self.log('login failed')
            return
        for url in self.after_login_urls:
            yield scrapy.Request(url, callback=self.parse_questions)

    def parse_questions(self, response):
        texts = response.xpath('//tr//a/text()').extract()
        links = response.xpath('//tr//a/@href').extract()
        data = list(zip(texts, links))
        names = ('text', 'url')
        return [dict(zip(names, item)) for item in data]

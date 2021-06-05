import os
import scrapy


class XSpider(scrapy.Spider):
    name = 'archiver'
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
        'http://quotes.toscrape.com/page/2/',
        'http://quotes.toscrape.com/page/3/',
        'http://quotes.toscrape.com/page/4/',
        'http://quotes.toscrape.com/page/5/',
        'http://quotes.toscrape.com/page/6/',
        'http://quotes.toscrape.com/page/7/',
        'http://quotes.toscrape.com/page/8/',
        'http://quotes.toscrape.com/page/9/',
        'http://quotes.toscrape.com/page/10/',
    ]

    def parse(self, response):
        num = response.url.split('/')[-2]
        dir = getattr(self, 'dstdir', 'html_files')
        os.makedirs(dir, mode=0o755, exist_ok=True)
        fname = 'quote-%s.html' % num
        fname = os.path.join(dir, fname)
        ofile = open(fname, 'w')
        ofile.write(response.text)

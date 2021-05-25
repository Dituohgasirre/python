import os
import sys
from datetime import datetime
import requests
from lxml import etree
import json
import time

# use Django models
BASEDIR = os.path.dirname(os.path.realpath(__file__))
DB_BASEDIR = os.path.join(BASEDIR, 'db')
sys.path.insert(0, DB_BASEDIR)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "db.settings")
#from store import models


def log(text):
    print(text, file=sys.stderr)


class Spider:

    def __init__(self, timeout=30, interval=0.3):
        # the default 'Usea-Agent' is not accepted by lagou.com
        headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.8",
        "Connection": "keep-alive",
        "Host": "www.lagou.com",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.109 Safari/537.36"
        }
        self.session = requests.Session()
        self.session.headers.update(headers)
        self.timeout = timeout
        self.interval = interval

    def id_from_url(self, url):
        x = url.split('/')[-1]
        x = x.split('.')[0]
        return x

    def get_one(self, url):
        job_id = self.id_from_url(url)

        try:
            text = self.fetch(url)
        except AssertionError:
            log('failed to download job %s' % job_id)
            return None

        # # no such record
        # if '你来晚了' in text:
        #     return None

        try:
            record = self.parse(text)
        except AssertionError:
            log('html source code error')
            return None
        else:
            record['job_id'] = job_id
            return record

    def fetch(self, url):
        count = 10
        for i in range(count):
            r = self.session.get(url, timeout=self.timeout)
            code = r.status_code
            if code == 200:
                return r.text
            elif code == 302:   # may be we are too fast.
                continue
        assert False, "failed to download"

    def get_first(self, tree, xpath):
        es = tree.xpath(xpath)
        assert es, "not found"
        return es[0]

    def parse(self, text):
        tree = etree.HTML(text)

        # job title
        xpath = '//div[@class="job-name"]/span[@class="name"]'
        job_title = self.get_first(tree, xpath).text

        # job salary, experence, education
        xpath = '//dd[@class="job_request"]//span/text()'
        info = [x.replace('/', '').strip() for x in tree.xpath(xpath)]
        job_salary, x, job_experence, job_education, x = info

        # job tags
        xpath = '//dd[@class="job_request"]//li/text()'
        job_tags = ':'.join(tree.xpath(xpath))

        # job advantage
        xpath = '//dd[@class="job-advantage"]/p/text()'
        job_advantage = self.get_first(tree, xpath)

        # job detail
        xpath = '//dd[@class="job_bt"]//p/text()'
        info = [x.replace('\xa0', '') for x in tree.xpath(xpath)]
        job_detail = '\n'.join(info)

        # job address
        xpath = '//div[@class="work_addr"]//text()'
        info = tree.xpath(xpath)
        info = ' '.join(info).split()[:-1]
        info = [x for x in info if x != '-']
        job_address = ''.join(info)

        # pub date
        xpath = '//p[@class="publish_time"]/text()'
        pub_date = self.get_first(tree, xpath).split('\xa0')[0]

        # company id
        xpath = '//dl[@class="job_company"]/dt/a'
        a = self.get_first(tree, xpath)
        url = a.attrib['href']
        company_id = self.id_from_url(url)

        # company name
        xpath = '//dl[@class="job_company"]/dt/a/img'
        x = self.get_first(tree, xpath)
        company_name = x.attrib['alt']

        # create time
        create_time = datetime.now()

        record = {}
        record['job_title'] = job_title
        record['job_salary'] = job_salary
        record['job_experence'] = job_experence
        record['job_education'] = job_education
        record['job_tags'] = job_tags
        record['job_advantage'] = job_advantage
        record['job_detail'] = job_detail
        record['job_address'] = job_address
        record['pub_date'] = pub_date
        record['create_time'] = create_time

        return record


if __name__ == '__main__':
    i = Spider()
    job_ids = range(20001, 21000)
    for id in job_ids:
        url = 'https://www.lagou.com/jobs/%s.html' % id
        record = i.get_one(url)
        if record is not None:
            open('%s.txt' % id, 'w').write(json.dumps(record))
        time.sleep(0.5)

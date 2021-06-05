#!/home/joshua/.pyenv/versions/webkit/bin/python

from selenium import webdriver

urls = [
    'http://www.goubanjia.com/index1.shtml',
    'http://www.goubanjia.com/index2.shtml',
    'http://www.goubanjia.com/index3.shtml',
    'http://www.goubanjia.com/index4.shtml',
    'http://www.goubanjia.com/index5.shtml',
    'http://www.goubanjia.com/index6.shtml',
    'http://www.goubanjia.com/index7.shtml',
    'http://www.goubanjia.com/index8.shtml',
    'http://www.goubanjia.com/index9.shtml',
    'http://www.goubanjia.com/index10.shtml',
]


def fetch(d, url):
    d.get(url)
    es = d.find_elements_by_xpath('//td[@class="ip"]')
    return [e.text for e in es]


if __name__ == '__main__':
    d = webdriver.PhantomJS()
    ips = []
    for url in urls:
        ips += fetch(d, url)

    for ip in ips:
        print(ip)

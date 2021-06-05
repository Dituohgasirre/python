import sys
import os

from lxml import etree
import requests


def fetch(url):
    r = requests.get(url)
    if r.status_code == 200:
        html = r.text
    else:
        html = None
    return html


def x(element):
    return '<%s>' % element.tag


def children(element):
    return element.xpath('*')


def parse(html):

    width = ' ' * 2

    def proc_children(element, indent=''):
        for child in children(element):
            print(indent, x(child), sep='')     # 输出自己
            proc_children(child, indent+width)  # 输出子节点

    tree = etree.HTML(html)
    print(x(tree))              # 输出自己
    proc_children(tree, width)  # 输出子节点


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('usage: %s url' % os.path.basename(sys.argv[0]))
        exit(1)

    url = sys.argv[1]
    html = fetch(url)
    parse(html)

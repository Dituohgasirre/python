# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import hashlib

import MySQLdb as db
from scrapy.exceptions import DropItem


def genid(item):
    text = '%s:%s:%s' % (item.get('text'), item.get('author'),
                         item.get('tags'))
    h = hashlib.sha1(text.encode())
    return h.hexdigest()


class UniquePipeline:

    def process_item(self, item, spider):
        item_id = genid(item)
        if item_id in self.all_ids:
            raise DropItem('item exists')
        else:
            self.all_ids.append(item_id)
            return item

    def open_spider(self, spider):
        self.all_ids = []


class IntegrityPipeline:

    def process_item(self, item, spider):
        for field in item.fields:
            if field not in item or item[field] is None:
                raise DropItem('invalid item')
        return item


class TextWriterPipeline:

    def open_spider(self, spider):
        self.file = open('items.txt', 'w')
    def close_spider(self, spider):
        self.file.close()
    def process_item(self, item, spider):
        for k in ['text', 'author', 'tags']:
            value = item[k]
            self.file.write('%s: %s\n' % (k, value))
        self.file.write('\n')
        return item


class SeparateFilePipeline:

    def process_item(self, item, spider):
        fmt = 'text: %(text)s\nauthor: %(author)s\ntags: %(tags)s\n'
        content = fmt % item
        fname = hashlib.sha1(content.encode()).hexdigest() + '.txt'
        with open(fname, 'w') as f:
            f.write(content)
        return item


class MysqlPipeline:

    def __init__(self, user, passwd, db, host, port, charset):
        self.user = user
        self.passwd = passwd
        self.db = db
        self.host = host
        self.port = port
        self.charset = charset

    def open_spider(self, spider):
        self.conn = db.connect(host=self.host, port=self.port,
                               user=self.user, passwd=self.passwd,
                               database=self.db, charset=self.charset)
        self.cur = self.conn.cursor()

    def close_spider(self, spider):
        self.conn.commit()
        self.conn.close()

    def process_item(self, item, spider):
        sql = 'insert into quotes values("%s", "%s", "%s")'
        args = (item['text'], item['author'], item['tags'])
        self.cur.execute(sql, args)
        self.conn.commit()

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            user = crawler.settings.get('DB_USER'),
            passwd = crawler.settings.get('DB_PASSWD'),
            db = crawler.settings.get('DB_DB'),
            host = crawler.settings.get('DB_HOST'),
            port = crawler.settings.get('DB_PORT'),
            charset = crawler.settings.get('DB_CHARSET')
        )

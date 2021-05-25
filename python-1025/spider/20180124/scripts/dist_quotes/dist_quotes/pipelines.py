# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

import MySQLdb as db


class DistQuotesPipeline(object):
    def process_item(self, item, spider):
        return item


class TextPipeline(object):
    def process_item(self, item, spider):
        text = json.dumps(item)
        self.file.write(text + '\n')
        return item

    def open_spider(self, spider):
        self.file = open('result.jl', 'w')

    def close_spider(self, spider):
        self.file.close()


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
        sql = 'insert into quotes values("%s", "%s", "%s", "%s")'
        args = (item['text'], item['author'], item['tags'], item['flag'])
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

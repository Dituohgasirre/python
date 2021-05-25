import MySQLdb
from scrapy.exceptions import DropItem


class QuotesPipeline(object):
    def process_item(self, item, spider):
        return item


class QuotesValidationPipeline:
    def process_item(self, item, spider):
        for field in item.fields:
            if field not in item:
                raise DropItem('field %s is required for item' % field)
        return item


class QuotesMysqlPipeline:
    tbname = 'quote'

    def __init__(self, user, passwd, db,
                 host='localhost', port=3306, charset='utf8'):
        self.user = user
        self.passwd = passwd
        self.db = db
        self.host = host
        self.port = port
        self.charset = charset

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            user=crawler.settings.get('DB_USER'),
            passwd=crawler.settings.get('DB_PASSWD'),
            db=crawler.settings.get('DB_DB'),
            host=crawler.settings.get('DB_HOST'),
            port=crawler.settings.get('DB_PORT'),
            charset=crawler.settings.get('DB_CHARSET')
        )

    def open_spider(self, spider):
        self.conn = MySQLdb.connect(host=self.host, port=self.port,
                                    user=self.user, passwd=self.passwd,
                                    database=self.db, charset=self.charset)
        self.cursor = self.conn.cursor()

    def close_spider(self, spider):
        self.conn.commit()
        self.conn.close()

    def process_item(self, item, spider):
        sql = 'insert into %s ' % self.tbname
        sql += 'values (%s, %s, %s)'
        data = (item['text'], item['author'], item['tags'])
        self.cursor.execute(sql, args=data)
        self.conn.commit()
        return item

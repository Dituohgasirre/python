BOT_NAME = 'dist_quotes'
SPIDER_MODULES = ['dist_quotes.spiders']
NEWSPIDER_MODULE = 'dist_quotes.spiders'
ROBOTSTXT_OBEY = False
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
SCHEDULER_PERSIST = True
ITEM_PIPELINES = {
    'scrapy_redis.pipelines.RedisPipeline': 301,
}
LOG_LEVEL = 'DEBUG'
# DOWNLOAD_DELAY = 3

# MySQL server info
DB_USER = 'scrapy'
DB_PASSWD = 'scrapy'
DB_DB = 'scrapy'
DB_HOST = 'localhost'
DB_PORT = 3306
DB_CHARSET = 'utf8'

# Redis server info
REDIS_HOST = '172.25.254.101'
REDIS_PORT = 6379

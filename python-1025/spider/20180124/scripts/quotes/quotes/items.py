import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, TakeFirst


def add_prefix(text):
    return 'author: ' + text


class QuotesItem(scrapy.Item):
    text = scrapy.Field()
    author = scrapy.Field(
                input_processor=MapCompose(str.strip, add_prefix)
            )
    tags = scrapy.Field()


class QuotesItemLoader(ItemLoader):
    default_item_class = QuotesItem
    default_input_processor = MapCompose(str.strip)
    default_output_processor = TakeFirst()

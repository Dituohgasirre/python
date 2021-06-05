import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, TakeFirst, Identity


def drop_symbol(text):
    return text[1:]


def urljoin(url, loader_context):
    response = loader_context['response']
    return response.urljoin(url)


class BooksItem(scrapy.Item):
    title = scrapy.Field()
    price = scrapy.Field()
    image_urls = scrapy.Field()
    images = scrapy.Field()


class BooksItemLoader(ItemLoader):
    default_item_class = BooksItem
    default_output_processor = TakeFirst()
    title_in = MapCompose(str.strip)
    price_in = MapCompose(drop_symbol, float)
    image_urls_in = MapCompose(urljoin)
    image_urls_out = Identity()

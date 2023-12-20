<<<<<<< HEAD
# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BoxofficeCrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    domestic_revenue = scrapy.Field()
    world_revenue = scrapy.Field()
    distributor = scrapy.Field()
    opening_revenue = scrapy.Field()
    opening_theaters = scrapy.Field()
    budget = scrapy.Field()
    MPAA = scrapy.Field()
    genres = scrapy.Field()
    in_release = scrapy.Field()
    release_date = scrapy.Field()
    pass
=======
# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BoxofficeCrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    domestic_revenue = scrapy.Field()
    world_revenue = scrapy.Field()
    distributor = scrapy.Field()
    opening_revenue = scrapy.Field()
    opening_theaters = scrapy.Field()
    budget = scrapy.Field()
    MPAA = scrapy.Field()
    genres = scrapy.Field()
    in_release = scrapy.Field()
    release_date = scrapy.Field()
    running_time = scrapy.Field()
    pass
>>>>>>> d9aefeb7390689c0e1f1a12d905964a735950e9a

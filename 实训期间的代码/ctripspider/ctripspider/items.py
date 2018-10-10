# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CtripspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    author_name = scrapy.Field()
    title = scrapy.Field()
    write_time = scrapy.Field()
    travel_days = scrapy.Field()
    travel_mouth = scrapy.Field()
    travel_cost = scrapy.Field()
    strategy = scrapy.Field()


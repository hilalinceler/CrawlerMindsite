# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CrawlermindsiteItem(scrapy.Item):
    id = scrapy.Field()
    userID = scrapy.Field()
    pass

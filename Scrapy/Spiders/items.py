# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SpidersItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    """在items里定义数据类型"""
    title=scrapy.Field()
    pic=scrapy.Field()
    url=scrapy.Field()

    jianjie=scrapy.Field()
    video_url=scrapy.Field()
    file_name=scrapy.Field()
    saved_video=scrapy.Field()

    pass

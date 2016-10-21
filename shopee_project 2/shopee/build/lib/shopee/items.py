# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ShopeeItem(scrapy.Item):
    item_id=scrapy.Field()
    item_name=scrapy.Field()
    shop_id=scrapy.Field()
    cat_id=scrapy.Field()
    cat_name=scrapy.Field()
    all_cat=scrapy.Field()
    item_price=scrapy.Field()
    item_likes=scrapy.Field()
    item_condition=scrapy.Field()
    item_time_ori=scrapy.Field()
    item_time=scrapy.Field()
    def __repr__(self):
        """only print out attr1 after exiting the Pipeline"""
        return repr({"item_id": self['item_id']})
    pass

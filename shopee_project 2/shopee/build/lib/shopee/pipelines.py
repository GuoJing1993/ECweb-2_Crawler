# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exceptions import DropItem
import numpy as np
import pandas as pd

class ShopeePipeline(object):
    def __init__(self):
        self.ids_seen = set()
        self.shop_ids_seen = set()
        #try:
        data=pd.read_csv('/Users/peternapolon/desktop/shopee_project/shopee/shopee/spiders/test.csv')
        data=data[data.item_time_ori != 'item_time_ori']
        self.last_time=data['item_time_ori'].max()
        #except:
        #    self.last_time=0
    def process_item(self, item, spider):
        if (item['item_id'] in self.ids_seen and item['shop_id'] in self.shop_ids_seen) or int(item['item_time_ori'])<=int(self.last_time):
            raise DropItem("Duplicate item found %s"%(self.last_time))
        else:
            self.ids_seen.add(item['item_id'])
            return item

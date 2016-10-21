import scrapy
from bs4 import BeautifulSoup
import json
import time
import re
from shopee.items import ShopeeItem
from scrapy.crawler import CrawlerProcess
import requests

class shopeeCrawler(scrapy.Spider):
    name='shopee_newest'
    pagelist=[]
    jscatcontent=requests.get('https://mall.shopee.tw/api/v1/category_list/').content

    global catdict
    catdict={}
    catid=re.findall('"catid": (\d+)',jscatcontent,re.S)
    catname=re.findall('{"display_name": "(.*?)"',jscatcontent,re.S)
    for i in range(len(catid)):
        catdict[str(catid[i])]=catname[i]

#    jsdict=json.loads(jscatcontent)
#    main_cat_id_list=[]
#    for cat in range(len(jsdict)):
#        main_cat_id=jsdict[cat]['main']['catid']
#        main_cat_id_list.append(str(main_cat_id))
    
#   for cat in main_cat_id_list:
#        for page in range(0,101,50):
#            pagelist.append('https://mall.shopee.tw/search/api/items/?page_type=search&match_id='+str(cat)+'&keyword=&shop_categoryids=&hashtag=&facet_type=&by=ctime&order=desc&newest='+str(page)+'&limit=50&need_drop_word=false')

    for page in range(0,301,50):
        pagelist.append('https://mall.shopee.tw/search/api/items/?page_type=search&match_id='+str(62)+'&keyword=&shop_categoryids=&hashtag=&facet_type=&by=ctime&order=desc&newest='+str(page)+'&limit=50&need_drop_word=false')

    start_urls=pagelist

    l=[]
    def parse(self, response):
        item_data=ShopeeItem()
        jscontent=response.body
        jsdict=json.loads(jscontent)
        jsitems=jsdict['items']
        id 
        for i in range(0,50):
            item_data['item_id']=jsitems[i]['itemid']
            try:
                item_data['item_name']=eval("u'%s'" %(jsitems[i]['name']))
            except:
                item_data['item_name']='Missing'
            item_data['shop_id']=jsitems[i]['shopid']
            item_data['cat_id']=jsitems[i]['catid']
            try:
                item_data['cat_name']=eval("u'%s'"%(catdict[str(jsitems[i]['catid'])]))
            except:
                item_data['cat_name']='Something wrong'
            try:
                item_data['all_cat']=",".join(eval("u'%s'"%(catdict[str(j)])) for j in jsitems[i]['cats'])
            except:
                item_data['all_cat']='Something wrong'
            item_data['item_price']=jsitems[i]['price']/100000
            item_data['item_likes']=jsitems[i]['liked_count']
            item_data['item_condition']=jsitems[i]['condition']
            item_data['item_time_ori']=int(jsitems[i]['mtime'])
            item_data['item_time']=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(jsitems[i]['mtime']))
            yield item_data
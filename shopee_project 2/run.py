# -*- coding: utf-8 -*-

import os
import time
import numpy as np
import pandas as pd

a='cat62+cat70+cat71+cat69'
l=[]
username=raw_input('Please enter username of this computer: ')
for i in range(0,24):
    x=time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime())
    os.system('cd /Users/'+username+'/desktop/shopee_project/shopee/shopee/spiders;scrapy crawl shopee_newest -o'+a+'_'+x+'.csv')
    l.append(a+'_'+x)
    os.system('cp /Users/'+username+'/desktop/shopee_project/shopee/shopee/spiders/'+a+'_'+x+'.csv /Users/'+username+'/dropbox/shopee_project/raw'+a+'_'+x+'.csv')
    time.sleep(1800)

finaldata=pd.DataFrame()

for i in l:
    mydata=pd.read_csv('/Users/'+username+'/desktop/shopee_project/shopee/shopee/spiders/'+i+'.csv', encoding='utf-8')
    finaldata=pd.concat([finaldata,mydata],axis=0)

finaldata.drop_duplicates(subset=['item_id','shop_id'])
M=raw_input('Please enter Month')
D=raw_input('Please enter Date')
H=raw_input('Please enter Hours')
Mi=raw_input('Please enter Minutes')
start_time=time.strptime('2016'+'-'+M+'-'+D+'-'+H+'-'+Mi+'-'+'00', "%Y-%m-%d-%H-%M-%S")
finaldata=finaldata[finaldata.item_time_ori>=int(time.mktime(start_time))]
finaldata.to_csv('/Users/'+username+'/desktop/shopee_project/shopee/shopee/spiders/test.csv', sep=',', encoding='utf-8')
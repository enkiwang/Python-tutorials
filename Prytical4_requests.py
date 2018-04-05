#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 16:08:15 2018
#1)urllib2: python module to fetch URLs (accept Request objs.)
#2)BeautifulSoup: python library for pulling data out of html and xml files
Needs to be improved: adding num_images argument
@author: yongweiw
"""

import re
import requests

# requests made from the clients and responses sent from servers
key = "cat"

url = 'http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=' + key + '&ct=201326592&v=flip'  #Baidu
#url = "https://www.google.co.in/search?q="+key+"&source=lnms&tbm=isch"   #Google
#req = urllib2.Request("https://arxiv.org/")
#header = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"}

results = requests.get(url)


pic_url = re.findall('"objURL":"(.*?)",', results.text, re.S)
print("Find key:"+ key + ", images downloading..")
k = 1
for url_ in pic_url:
    print("Downloading" + str(k) + "-th image, url:" + str(url_))
    try:
        pic = requests.get(url_, timeout=5)
    except requests.exceptions.ConnectionError:
        print("images cannot be downloaded")
        continue
    
    dir_ = './images_crawler_test/' + key + '_' + str(k) + '.jpg'
    fp = open(dir_, "wb")
    fp.write(pic.content)
    fp.close()
    k += 1
    print(k+"images have been downloaded!")
    
    
    





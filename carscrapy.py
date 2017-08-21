# -*- coding: utf-8 -*-
import csv
import urllib
from bs4 import BeautifulSoup
import sys

# 卡车之家报价首页
mainpage = 'http://product.360che.com/1.html'


# 数据抓取
def CarInfoDownload(url):
    html = urllib.urlopen(url)
    bsobj = BeautifulSoup(html, 'lxml')
    table = bsobj.find_all('div', attrs={'class': 'content'})[0]
    for el in table.find_all('a'):
        print el


# 数据存储pp

if __name__ == '__main__':
    CarInfoDownload(mainpage)

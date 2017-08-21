# encoding: utf-8
import time
from selenium import webdriver
import lxml
import urllib
import random
import datetime
from bs4 import BeautifulSoup
import os


pages = set()
random.seed(datetime.datetime.now())
web_name = 'http://www.mtime.com/'


def getLinks(pageUrl):
    global pages
    html = urllib.urlopen('http://www.mtime.com/'+pageUrl)
    bs = BeautifulSoup(html, 'lxml')
    try:
        pass
    except AttributeError:
        print "出错啦"
    for link in bs.find_all('a'):
        if link.attrs['href'] not in pages:
            newpage = link.attrs['href']
            # print ('----------'+newpage)
            pages.add(newpage)
            getLinks(newpage)


if __name__ == '__main__':
    getLinks("")
    with open(r'd:\recoder.txt', 'w') as fp:
        for d in pages:
            if str(d).startswith('http'):
                print d
                fp.write(d+'\n')
            else:
                continue




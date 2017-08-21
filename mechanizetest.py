# encoding: utf-8
import urllib
import mechanize
import lxml.etree
import lxml
from lxml.cssselect import CSSSelector
import sys
from bs4 import BeautifulSoup
from selenium import webdriver
import time

pages = set()


def getlinks(pageUrl):
    global pages
    html = urllib.urlopen(pageUrl + pageUrl)


def parse_form(html):
    #print html
    h = lxml.etree.HTML(html)
    sel = CSSSelector('form input')
    data = {}
    for e in sel(h):
        #print 'in'
        if e.get('name'):
            data[e.get('name')] = e.get('value')
#             print data
    print data
    return data


if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf-8')
    br = mechanize.Browser()
    driver = webdriver.PhantomJS(executable_path=r'D:\phantomjs-2.1.1-windows\bin\phantomjs')
    #设置bookie
    cj = mechanize.CookieJar()
    br.set_cookiejar(cj)

    # 参数设置
    LocalUrl = 'http://www.wxclgl.com/qms/'
    Login_user = 'infinit'
    Login_password = '123456'

    # 定义及打开浏览器
    br.open(LocalUrl)
    br.select_form(nr=0)
    # 设置请求值
    br['userName'] = Login_user
    br['password'] = Login_password
    response = br.submit()
    driver.get(br)
    print br
    # br.open(br.geturl()+r'/serviceGarage/companyList.jsp?_=1496209997522')
    # print response.read()

    # driver.get_screenshot_as_file('D:\catch.png')
    # time.sleep(5)
    # driver.close()

    # for lk in br.links():
    #     if hasattr(lk, 'attrs'):
    #         for o in lk.attrs:
    #             if o[0] == 'cmshref':
    #                 # br.open(LocalUrl+'/'+o[1])
    #                 print o[1]





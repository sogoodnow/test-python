# -*- coding: utf-8 -*-
import csv
import urllib
from bs4 import BeautifulSoup
import sys
reload(sys)
sys.setdefaultencoding('utf8')

# html = urllib.urlopen('https://en.wikipedia.org/wiki/Comparison_of_text_editors')
html = urllib.urlopen('http://www.proxy360.cn')
bsObj = BeautifulSoup(html, 'lxml')

# table = bsObj.find_all('table', {"class": "wikitable"})[0]
# rows = table.find_all("tr")
div = bsObj.find_all('div', {"class": "proxylistitem"})
rows = bsObj.find_all('span', {"class": "tbBottomLine"})
# print rows

global i
i = 03
r = list()
csvFile = open(r'D:\content.csv', 'w')
writer = csv.writer(csvFile)
try:
    for row in rows:
        i += 1
        if '速度测评'.encode('GBK') in row.get_text().strip().encode('GBK') :
            i -= 1
            continue
        else:
            r.append(row.get_text().strip().encode('GBK'))
        if i % 8 == 0:
            i = 0
            writer.writerow(r)
            r = list()
finally:
    csvFile.close()



# try:
#     for row in rows:
#         csvRow = []
#         for cell in row.find_all(['span']):
#             csvRow.append(cell.get_text())
#         writer.writerow(csvRow)
# finally:
#     csvFile.close()

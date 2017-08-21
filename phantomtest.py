#!/usr/bin/python
# coding:utf-8
from selenium import webdriver
import time
from selenium.webdriver.support.select import Select

driver = webdriver.PhantomJS(executable_path=r'D:\phantomjs-2.1.1-windows\bin\phantomjs')
driver.set_window_size('1920', '1080')
driver.get('http://www.wxclgl.com/qms/')
time.sleep(3)
name = driver.find_element_by_id('userName')
pas = driver.find_element_by_id('password')
btn = driver.find_element_by_id('Submit')
name.send_keys('infinit')
pas.send_keys('123456')
btn.click()
time.sleep(6)
js = "var d = document.getElementById('menu_div');var aa=d.querySelectorAll('.panel-body')[2].style.display='block';" \
     "d.querySelectorAll('li>ul')[4].style.display='block';"
driver.execute_script(js)
driver.find_element_by_link_text('车辆基本信息').click()
time.sleep(60)
sel = driver.find_element_by_class_name('pagination-page-list')
Select(sel).select_by_index(4)
time.sleep(60)
driver.save_screenshot('D:\ccc.jpg')
global i
i = 0
table = driver.find_element_by_class_name("datagrid-view2").find_element_by_class_name('datagrid-body')
for tr in table.find_elements_by_class_name('datagrid-row'):
     j = 0
     for cell in tr.find_elements_by_class_name('datagrid-cell'):
          j += 1
          if cell.text:
               print cell.text
          else:
               print '无'
          print j
     i += 1
     print i
driver.close()


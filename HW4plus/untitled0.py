# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 21:09:02 2018

@author: breezefay
"""

import requests

from lxml import etree
import urllib

def get_web_page(url):
    resp = requests.get(
        url=url,
        cookies={'over18': '1'}
    )
    if resp.status_code != 200:
        print('Invalid url:', resp.url)
        return None
    else:
        return resp.text
    
aa = input("input:")

print("你搜尋的是:"+ aa)

#print(urllib.request.quote(a))

a = urllib.request.quote(aa)
#a = urllib.quote(a.decode(sys.stdin.encoding).encode('utf8'))
#print(a)

r = ("https://www.nuwainfo.com/zh/blog/?page=1#")##1~4
    
print("你搜尋的網址是"+r)

page = get_web_page(r)
#soup = BeautifulSoup(page)

#print(LC20lb.select('.LC20lb')[1].text)

#x = soup.find_all("//a/@href")

#print(x)
#print(soup)
sel = etree.HTML(page)

###可能要修改一下

for i in sel.xpath('/html/body/div[4]/div/div/div[1]/div[4]/div[1]/div[1]/h2/a'):
    print(str(aa)+i)
    
    #for each in sel.xpath('//*[@id="ires"]/ol/div[position()]/div/div/cite/text()'):
        #print(each)
    

#xx = selectSite.select_by_value(cite)


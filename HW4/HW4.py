# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 14:21:18 2018

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

r = ("https://www.google.com.tw/search?q="+str(a)+"&oq="+str(a)+"&aqs=chrome..69i57j0l5.1277j1j1&sourceid=chrome&ie=UTF-8")
    
print("你搜尋的網址是"+r)

page = get_web_page(r)
#soup = BeautifulSoup(page)

#print(LC20lb.select('.LC20lb')[1].text)

#x = soup.find_all("//a/@href")

#print(x)
#print(soup)
sel = etree.HTML(page)

for each in sel.xpath('//*[@id="ires"]/ol/div[position()>=0]/h3/a/text()'):
    print(str(aa)+each)
    for each in sel.xpath('//*[@id="ires"]/ol/div[2]/div/div/cite/text()'):
        print(each)
    

#xx = selectSite.select_by_value(cite)
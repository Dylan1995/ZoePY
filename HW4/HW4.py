# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 14:21:18 2018

@author: breezefay
"""

import requests

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
    
a = input("input:")

print("你搜尋的是:"+ a)

#print(urllib.request.quote(a))

a = urllib.request.quote(a)
#a = urllib.quote(a.decode(sys.stdin.encoding).encode('utf8'))
#print(a)

r = ("https://www.google.com.tw/search?q="+str(a)+"&oq="+str(a)+"&aqs=chrome..69i57j0l5.1277j1j1&sourceid=chrome&ie=UTF-8")
    
print("你搜尋的網址是"+r)

page = get_web_page(r)
if page:
	print(page)
    
    
   # https://www.google.com.tw/search?q=%E6%99%BA%E9%9A%9C&oq=%E6%99%BA%E9%9A%9C&aqs=chrome..69i57j69i60l2j0l3.3850j0j1&sourceid=chrome&ie=UTF-8
#https://www.google.com.tw/search?q=%E6%99%BA%E9%9A%9C&oq=%E6%99%BA%E9%9A%9C&aqs=chrome..69i57j69i60l2.1775j0j1&sourceid=chrome&ie=UTF-8
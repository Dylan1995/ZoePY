import re
import requests
import datetime

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
    
    


for i in range(1,5):
    index = str(i)
    
    Target_url = ("https://www.nuwainfo.com/zh/blog/?page="+ index + "#")
    page = get_web_page(Target_url)
    sel = etree.HTML(page)
    title = []
    for each in sel.xpath('/html/body/div[4]/div/div/div[1]/div[4]/div[position()>0]/div[position()>0]/h2/a/text()'):
        title.append(each)
        print(title)

    ReData = []    
    for i in sel.xpath('/html/body/div[4]/div/div/div[1]/div[4]/div[position()>0]/div[position()>0]/label/text()'):
    
        ReData.append(i)
    for data in ReData:
        d = re.findall(r"by\s(\w+)\s([\w\s,]+)", data)
    #print(d) # [("", ""),]
        author = d[0][0]
        date = d[0][1] # datetime.strptime("4 30, 2018", "%m %d, %Y")
        if "十二月" in date:
            date = date.replace("十二月","12") 
        if "十一月" in date:
            date = date.replace("十一月","11") 
        if "十月" in date:
            date = date.replace("十月","10") 
        if "九月" in date:
            date = date.replace("九月","9")
        if "八月" in date:
            date = date.replace("八月","8")
        if "七月" in date:
            date = date.replace("七月","7") 
        if "六月" in date:
            date = date.replace("六月","6") 
        if "五月" in date:
            date = date.replace("五月","5") 
        if "四月" in date:
            date = date.replace("四月","4") 
        if "三月" in date:
            date = date.replace("三月","3") 
        if "二月" in date:
            date = date.replace("二月","2")
        if "一月" in date:
            date = date.replace("一月","1") 
        cday = datetime.datetime.strptime(date, "%m %d, %Y")
        
        for i in title:
            print(i +"\n" + author + "\t" + str(cday))
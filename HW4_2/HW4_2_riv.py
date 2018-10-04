import re
import requests
import datetime
import json

from lxml import etree

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
mon_mand = ["一月","二月","三月","四月","五月","六月","七月","八月","九月","十月","十一月","十二月"]
mon_arab = ["1","2","3","4","5","6","7","8","9","10","11","12"]
  

page_num = 1 
title = []


while True:
    index = str(page_num)
    
    Target_url = ("https://www.nuwainfo.com/zh/blog/?page="+ index + "#")
    
    page = get_web_page(Target_url)
    if page == None:
        print("文章擷取完畢")
        break

    else:
        sel = etree.HTML(page)
        
        for i in sel.xpath('//div[position()>0]/div[position()>0]/div[position()>0]'):
            ti_arc = i.xpath("//h2/a/text()")
            rev_dat = i.xpath("//label/text()")
            url_add = i.xpath('/a/@herf')
                
            
            #print(url_add)
            
            
            for data in rev_dat:
                d = re.findall(r"by\s(\w+)\s([\w\s,]+)", data)
                
                author = d[0][0]
                date = d[0][1] # datetime.strptime("4 30, 2018", "%m %d, %Y")
                
                for mon in mon_mand:
                    
                    if mon in date:
                        i = mon_mand.index(mon)
                        date = date.replace(mon ,mon_arab[i])
                    

                cday = datetime.datetime.strptime(date, "%m %d, %Y")
                
                
                #u = str(author+"\t" + str(cday))
                dict2 = {}
                dict2["url"] = url_add
                dict2["title"] = str(ti_arc[0])
                dict2["author"] = str(author)
                dict2["date"] = str(cday)
                
                title.append(dict2)

                

        
        page_num += 1
print(title)


title = json.dumps(title)
fileObject = open('jsonFile.json', 'w')
fileObject.write(title)
fileObject.close()

    
        
   
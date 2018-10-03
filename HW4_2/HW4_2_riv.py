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
Mon_Mand = ["一月","二月","三月","四月","五月","六月","七月","八月","九月","十月","十一月","十二月"]
Mon_Arab = ["1","2","3","4","5","6","7","8","9","10","11","12"]
  
j = 1
page_num = 1 
while j == 1:
    index = str(page_num)
    
    Target_url = ("https://www.nuwainfo.com/zh/blog/?page="+ index + "#")
    
    page = get_web_page(Target_url)
    if page == None:
        print("文章擷取完畢")
        break

    else:
        sel = etree.HTML(page)
        title = []
        for i in sel.xpath('/html/body/div[4]/div/div/div[1]/div[4]/div[position()>0]/div[position()>0]'):
            ti_arc = i.xpath("//h2/a/text()")
            rev_dat = i.xpath("//label/text()")
            url_add = i.get("//h2/a/@herf")
            
            
            for data in rev_dat:
                d = re.findall(r"by\s(\w+)\s([\w\s,]+)", data)
                
                author = d[0][0]
                date = d[0][1] # datetime.strptime("4 30, 2018", "%m %d, %Y")
                
                for mon in Mon_Mand:
                    
                    if mon in date:
                        i = Mon_Mand.index(mon)
                        date = date.replace(mon ,Mon_Arab[i])
                    

                cday = datetime.datetime.strptime(date, "%m %d, %Y")
                
                #u = str(author+"\t" + str(cday))
                
                ini_li = ["","","",""]
                
                ini_li[0] = ("url"+":"+str(url_add))
                ini_li[1] = ("title"+":"+ str(ti_arc))
                ini_li[2] = ("author"+":"+author)
                ini_li[3] = ("date"+":"+str(cday))
                
                title.append(ini_li)
                #title = title.append(pppp)
                #print(author+"\t" + str(cday))
                #print(title)
                

        
        page_num += 1

title = json.dumps(title)
fileObject = open('jsonFile.json', 'w')
fileObject.write(title)
fileObject.close()

    
        
   
import urllib.request as request
import urllib.error as error
import time
import re

'''
下载页面
'''
def download(url,user_agent="wswp",num_retries=1 ):
    print("download url:",url)
    #设置用户代理
    headers = {"User-agent":user_agent}
    req = request.Request(url,headers=headers)
    try:
        html = request.urlopen(req).read().decode("utf-8")
    except error.URLError as e:
        print("download error:",e.reason)
        html = None
        if num_retries > 0:
            if hasattr(e,"code") and 500 <= e.code <= 600:
                return download(url,num_retries-1)
    return html



r = ("https://www.nuwainfo.com/zh/blog/?page=4#")  ##要下載1~4頁

page = get_web_page(r)

sel = etree.HTML(page)



def parsePage(pageHTML):
    links = re.findall("<li class=\"blog-unit\">.*?<a href=\"(.*?)\".*?>.*?<h3.*?>(.*?)</h3>.*?([0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2}).*?</li>",html,re.M|re.S) #
    for link in links:
        datas = []
        for data in link:
            data = data.replace("\n","")
            data = data.replace("\t","")
            datas.append(data)


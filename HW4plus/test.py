import re
import urllib.request as request
import urllib.error as error


def download(url, user_agent='wswp',  num_retries = 2):
    print ("download url :", url)
    headers = {'User-agent': user_agent}
    req = request.Request(url, headers=headers)
    try:
        html = request.urlopen(req).read().decode("utf-8")
    except error.URLError as e:
        print ('Download error:', e.reason)
        html = None
        if num_retries > 0:
            if hasattr(e, 'code') and 500 <= e.code <= 600:
                return download(url, num_retries-1)
    return html



def writeAricleToFile(aparams):
    html = download(aparams.pop(0))

    #文件名称
    atitle = aparams.pop(0)
    atitle = atitle.replace("/","-")
    atitle = atitle.replace(":","-")
    adate = aparams.pop(0)
    adate = adate.replace(" ","_")
    adate = adate.replace(":","-")
    fileName = "C:/Users/Administrator/Desktop/breezefay/"+adate+"_"+atitle+".txt"

    #文件内容
    content = parseArticleContent(html)
    content = content[0][1]
    #文件内容中去掉html标签
    content = re.sub("<.*?>", "", content, flags=re.M|re.S)
    content = content.replace("&lt;","<")
    content = content.replace("&gt;",">")
    print(fileName)
    f = open(fileName,"w+",encoding="utf-8")
    f.write(content)
    f.close()

def parsePage(pageHTML):
    links = re.findall("<li class=\"blog-unit\">.*?<a href=\"(.*?)\".*?>.*?<h3.*?>(.*?)</h3>.*?([0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2}).*?</li>",html,re.M|re.S) #
    for link in links:
        datas = []
        for data in link:
            data = data.replace("\n","")
            data = data.replace("\t","")
            datas.append(data)
        writeAricleToFile(datas)


if __name__ == '__main__':
    url = "https://www.nuwainfo.com/zh/blog/"
    html = download(url)
    parsePage(html)
    page_links = re.findall("<li class=\"page-item.*?<a href=\"(.*?)\".*?</li>",html,re.M|re.S)

    maxPageNum = 1
    for page_link in page_links:
        pageNum = int(page_link[page_link.rfind("/")+1:])
        if pageNum > maxPageNum:
            maxPageNum = pageNum

    pageUrl = "https://www.nuwainfo.com/zh/blog/article/list/"

    pageNum = 2
    while pageNum <= maxPageNum:
        newPageUrl = pageUrl + str(pageNum)
        html = download(newPageUrl)
        parsePage(html)
        pageNum = pageNum + 1


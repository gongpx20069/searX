# -*- coding:utf-8 -*-
import requests
from lxml import etree
import sys
import os
reload(sys)
sys.setdefaultencoding("utf-8")

def getfromsearX(word):
    if not os.path.exists(word):
    	os.mkdir(word)
    print '[+]searching '+word
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, compress',
        'Accept-Language': 'en-us;q=0.5,en;q=0.3',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'
        }
    #可以修改range(1,x)中的x的值，代表需要爬取的信息最后一页
    for pagecount in range(1, 11):
        url = 'https://searx.me/?q='+word+'&categories=general&pageno=' + str(pagecount)+'&time_range=None'
        html = requests.get(url=url,headers=headers)
        print '[+]'+url
        path = etree.HTML(html.content)
        flag=11
        if pagecount==1:
            flag=22
        for i in range(1,flag):
            tempword = ""
            for j in path.xpath('.//*[@id="main_results"]/div[%d]/h4/a//text()'%i):
                tempword+=j
            pageurl = path.xpath(".//*[@id='main_results']/div[%d]/h4/a/@href"%i)
            if pageurl:
                tempword = word+"/"+tempword+".html"
                try:
                    line = requests.get(pageurl[0],headers).content
                    with open(tempword,'w') as f:
                        f.write(line)
                        pass
                    print "[+]"+tempword
                except:
                    print "[-]"+tempword
                    pass
        print '[+]page '+str(pagecount)

#爬虫会将网页下载到本地目录
def main():
    find = raw_input("Please input :")
    getfromsearX(find)

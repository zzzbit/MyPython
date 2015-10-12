'''
Created on 2015年3月17日

@author: zhangzhizhi
'''
import urllib.request
import re

def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read().decode()
    return html
html = getHtml("http://www.baidu.com")
print(html)
def fetch(html):
    return re.compile(r"(www.+?)[^a-z/\._0-9]").findall(html)
print(fetch(html))
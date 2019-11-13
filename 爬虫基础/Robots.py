import requests
import re
import os
from bs4 import BeautifulSoup
import bs4
import string
import jieba

'''
def getHtmlText(url):
    try:
        r = requests.get("url", timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "获取失败"


if __name__ == "__main__":
    url_input = input("input your url: ")
    url = "https://" + url_input
    print(getHtmlText("https://" + url))
'''
# ----------------------code not test pass----------------------

'''
kv = {'wd': "woshishei"}
url = 'http://www.baidu.com/s'
r = requests.get(url, params=kv)
print(r.request.url)
print(r.status_code)
r.encoding=r.apparent_encoding
print(r.text)
'''

# ----------------------code test pass----------------------

'''

def getResource(url, head, param):  # 这个如何定义多个形参时，可传递任意个
    try:
        r = requests.get(url, headers=head)
        # print(r.request.url)
        # print(r.request.headers)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.content
    except:
        print("Something Worry")


if __name__ == '__main__':
    os.path = 'D:\\Temp&Files\\'
    h = {'User-Agent': 'Mozilla/5.0'}
    url = str.strip(input("Gvie me the Url: "))
    print(url)
    path = os.path + url.split('/')[-1]
    print(path)
    f = open(path, 'wb')
    f.write(getResource(url, h, h))
    # print(getResource(url, h, h))
    f.close()
    
'''
# ----------- get html resource to local file -----

'''
ip = input('input search ip: ')
url = 'http://www.ip138.com/ips138.asp?ip=' + ip + '&action=2'
print(url)
ug = {'User-Agent': 'Mozilla/5.0'}

r = requests.get(url, headers=ug)
print(r.status_code)
r.encoding = r.apparent_encoding


pattern = re.compile(u"[\u4e00-\u9fa5]+")  # 定义中文匹配的正则表达式
data = re.findall(pattern, r.text)  # 找出字符序列中的中文内容
print(data)
'''
# ----- ip belongs to area search --------------
'''
ip = input('input search ip: ')
url = 'http://www.ip138.com/ips138.asp?ip=' + ip + '&action=2'
print(url)
ug = {'User-Agent': 'Mozilla/5.0'}

r = requests.get(url, headers=ug)
print(r.status_code)
r.encoding = r.apparent_encoding

demo = r.text
soup = BeautifulSoup(demo, 'html.parser')
print(soup.prettify())
'''


def getHTMLText(url):
    ug = {'User-Agent': 'Mozilla/5.0'}
    try:
        r = requests.get(url, headers=ug, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text

    except requests.exceptions.HTTPError:
        return ""


def fillUnivList(ulist, html):
    soup = BeautifulSoup(html, "html.parser")
    for tr in soup.find('tbody').children:
        if isinstance(tr, bs4.element.Tag):
            tds = tr('td')
            ulist.append([tds[0].string, tds[1].string, tds[3].string])


def printUnivList(ulist, num):
    # print("{:^10}\t{:^6}\t{:^10}".format("排名", "学校", "分数"))   # 这行存在中文对其问题
    print("{0:^10}\t{1:{3}^10}\t{2:^10}".format("排名", "学校", "分数", chr(12288)))
    for i in range(num):
        u = ulist[i]
        print("{0:^10}\t{1:{3}^10}\t{2:^10}".format(u[0], u[1], u[2], chr(12288)))


def main():
    uinfo = []
    url = 'http://www.zuihaodaxue.cn/zuihaodaxuepaiming2019.html'
    html = getHTMLText(url)
    fillUnivList(uinfo, html)
    printUnivList(uinfo, 50)

main()

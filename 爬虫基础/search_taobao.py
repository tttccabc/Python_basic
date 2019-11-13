import requests
import re
import bs4
from bs4 import BeautifulSoup

def getHTMLText(url):
    # ug = {'User-Agent': 'Mozilla/5.0'}
    try:
        # r = requests.get(url, headers=ug, timeout=20)
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        # print(r.request.headers)
        return r.text
    except requests.HTTPError:
        print("GetHTMLText Error!")
        return ""


def parsePage(ilt, html):
    try:
        plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"', html)
        tlt = re.findall(r'\"raw_title\"\:\".*?\"', html)
        for i in range(len(plt)):
            price = eval(plt[i].split(':')[1])
            title = eval(tlt[i].split(':')[1])
            ilt.append([price, title])
    except:
        print("Parser Error")


def printGoodsList(ilt):
    tplt = "{:4}\t{:8}\t{:16}"
    print(tplt.format("序号", "价格", "商品名称"))
    count = 0
    for g in ilt:
        count += 1
        print(tplt.format(count, g[0], g[1]))


def main():
    goods = '球'
    depth = 2
    start_url = 'https://s.taobao.com/search?q=' + goods
    infoList = []
    for i in range(depth):
        try:
            url = start_url + '&s=' + str(44 * i)
            html = getHTMLText(url)
            parsePage(infoList, html)
        except:
            print(" Main Exception ")
    printGoodsList(infoList)


main()

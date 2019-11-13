"""
    目标:获取上交所 深交所 所有股票名称 交易信息
    输出:保存到文件中

    技术路线: request-bs4-re

    新浪股票/百度股票
"""

import requests
from bs4 import BeautifulSoup
import re
import traceback


def getHTMLText(url, code='utf-8'):
    ug = {'User-Agent': 'Mozilla/5.0'}
    try:
        r = requests.get(url, headers=ug, timeout=30)
        r.raise_for_status()
        r.encoding = code
        return r.text
    except requests.HTTPError:
        return ""
    #   print(traceback)


def getStockList(lst, stockURL):
    soup = BeautifulSoup(getHTMLText(stockURL), "html.parser")
    # print(soup)
    a = soup.find_all('a')
    for i in a:
        try:
            href = i.attrs['href']
            lst.append(re.findall(r's[hz]\d{6}', href)[0])
        except:
            continue
    # print('ending list')


def getStockInfo(lst, stockURL, fpath):
    count = 0
    for stock in lst:
        url = stockURL + stock + '.html'
        # print(url)
        html = getHTMLText(url)
        try:
            if html == '':
                continue
            infoDict = {}
            soup = BeautifulSoup(html, 'html.parser')
            # print(soup)
            stockInfo = soup.find('div', attrs={'class': 'stock-bets'})
            # print(stockInfo)
            #  print(stockInfo)
            # name=soup.find('div',attrs={'class':'bets-name'})
            name = soup.find('a', attrs={'class': 'bets-name'})
            # print(name)
            # print(name)
            infoDict.update({'股票名称': name.text.split()[0]})
            #  print(infoDict)

            # print(stockInfo)
            keyList = stockInfo.find_all('dt')
            # print(keyList)
            valueList = stockInfo.find_all('dd')
            # print(valueList)
            for i in range(len(keyList)):
                key = keyList[i].text
                val = valueList[i].text
                infoDict[key] = val
            with open(fpath, 'a', encoding='utf-8') as f:
                f.write(str(infoDict) + '\n')
                count = count + 1
                print('\r当前速度：{:.2f}%'.format(count * 100 / len(lst)), end='')
        except:
            count = count + 1
            print('\r当前速度：{:.2f}%'.format(count * 100 / len(lst)), end='')
            # traceback.print_exc()
            continue


def main():
    stock_list_url = 'http://quote.eastmoney.com/stock_list.html'
    stock_info_url = 'https://gupiao.baidu.com/stock/'
    output_file = 'D:/BaiduStockInfo.txt'
    slist = []
    getStockList(slist, stock_list_url)
    getStockInfo(slist, stock_info_url, output_file)


main()

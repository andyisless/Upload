# -*- coding: utf-8 -*-
# @Time : 2020/2/24 下午7:27
# @Author : www.Andy.ge
# @FileName: Bili-Webp-Onepage.py
# @Software: Python3 @ PyCharm
# @Blog ：项目地址 自己写的，下载bilibili的webp的图片！突破性的成果，一天的研究？浪费啊

import requests
import os
from bs4 import BeautifulSoup

def Geturl(url):
    headers = {
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) '
                              'AppleWebKit/537.36 (KHTML, like Gecko)'
                              ' Chrome/58.0.3029.110 Safari/537.36'}

    #html = requests.get(url, headers=headers)  # 获得elements里的所有代码
    #print(html.text)
    all_url = requests.get(url, headers=headers)
    soup = BeautifulSoup(all_url.text,'lxml')
    all_a = soup.find('div', class_="article-holder").find_all('img')       #重点是soup的寻找！

    root = "/Users/imac/desktop/"
    #path = root + data.split('/')[-1]
    for a in all_a:
        data = a['data-src']
        path = root + data.split('/')[-1]
        image_url = "http:" + data              #灵活修改地址
        print(image_url)
        try:
            if not os.path.exists(root):
                os.mkdir(root)
            if not os.path.exists(path):
                r = requests.get(image_url)
                r.raise_for_status()
                with open(path, 'wb') as f:
                    f.write(r.content)
                    f.close()
                    print("Downloaded")
            else:
                print("Existed")
        except:
            print("Failed")

if __name__ == '__main__':
    url = "https://www.bilibili.com/read/cv937865/"
    Geturl(url)
# -*- coding: utf-8 -*-
# @Time : 2020/2/20 下午5:52
# @Author : www.Andy.ge
# @FileName: Beautysoup.py
# @Software: Python3 @ PyCharm
# @Blog ：项目地址 https://blog.csdn.net/baidu_35085676/article/details/68958267

import requests
from bs4 import BeautifulSoup
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 UBrowser/6.1.2107.204 Safari/537.36'}

url = 'http://www.mzitu.com'

html = requests.get(url,headers = header)
#print(html.text) #打印输出看F12的网页源代码

"""
2.寻找所需信息
切换浏览器，右键‘查看网页源代码’，可以发现有很多这样的信息
<li><a href="http://www.mzitu.com/89334" target="_blank"><img width='236' height='354' class='lazy' alt='我是标题我是标题我是标题我是标题我是标题我是标题' src='http://i.meizitu.net/pfiles/img/lazy.png' data-original='http://i.meizitu.net/thumbs/2017/04/89334_02b06_236.jpg' /></a><span><a href="http://www.mzitu.com/89334" target="_blank">我是标题我是标题我是标题我是标题我是标题我是标题我是标题我是标题我是标题我是标题</a></span><span class="time">2017-04-02</span><span class="view">6,788次</span></li>

那么我们只需要提取这些东西就可以了…but:我写不出这么复杂的正则！！！没关系，我们的神器BeautifulSoup要上场了！
我们的步骤是：
①将获取的源码转换为BeautifulSoup对象
②搜索需要的数据
"""
soup = BeautifulSoup(html.text,'html.parser')   #自带的html.parser解析

"""
all_a = soup.find('div',class_='postlist').find_all('a',target='_blank')

soup.find('figure',class_='img_box').find_all('img,target='_src')
for a in all_a:
    title = a.get_text()
#    print(title) #输出套图的中文标提


注意：BeautifulSoup()返回的类型是<class 'bs4.BeautifulSoup'>
find()返回的类型是<class 'bs4.element.Tag'>
find_all()返回的类型是<class 'bs4.element.ResultSet'>
<class 'bs4.element.ResultSet'>不能再进项find/find_all操作
"""

"""
3.进入下载

点进一个套图之后，发现他是每个页面显示一个图片。

比如http://www.mzitu.com/26685是某个套图的第一页，后面的页数都是再后面跟/和数字http://www.mzitu.com/26685/2 (第二页).
那么很简单了，我们只需要找到他一共多少页，然后用循环组成页数就OK了。


#最大页数在span标签中的第10个？？
pic_max = soup.find_all('span')[10].text
#pic_max = 图片的地址！

print(pic_max)


#输出每个图片页面的地址
for i in range(1,int(pic_max) + 1):
    href = url+'/'+str(i)
    print(href)



#输出每个图片页面的地址
for i in range(1,int(pic_max) + 1):
    href = url+'/'+str(i)
    #print(href)
"""
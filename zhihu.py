# -*- coding: utf-8 -*-
# @Time : 2020/2/20 下午5:19
# @Author : www.Andy.ge
# @FileName: zhihu.py 打印知乎的详情
# @Software: Python3 @ PyCharm
# @Blog ：项目地址

import requests
import re
from bs4 import BeautifulSoup

headers={"User-Agent":"","Cookie":""}
zh_url = "https://www.zhihu.com/billboard"
zh_response = requests.get(zh_url,headers=headers)

webcontent = zh_response.text
soup = BeautifulSoup(webcontent,"html.parser")
script_text = soup.find("script",id="js-initialData").get_text()
rule = r'"hotList":(.*?),"guestFeeds"'
result = re.findall(rule,script_text)

temp = result[0].replace("false","False").replace("true","True")
hot_list = eval(temp)
print(hot_list)
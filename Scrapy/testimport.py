# -*- coding: utf-8 -*-
# @Time : 2020/2/20 下午5:19
# @Author : www.Andy.ge
# @FileName: umei.py
# @Software: Python3 @ PyCharm
# @Blog ：项目地址 https://www.jianshu.com/p/8cd7cb9ab64c

import requests
import os
from requests.packages import urllib3
from pyquery import PyQuery as pq

def get_url1(url):
# 模拟浏览器，不用改，几乎固定
    headers = {
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) '
                              'AppleWebKit/537.36 (KHTML, like Gecko)'
                              ' Chrome/58.0.3029.110 Safari/537.36'
                              }
    urllib3.disable_warnings()                                    #  预警作用
    html = requests.get(url, headers=headers, verify=False).text  # 获得elements里的所有代码
    doc = pq(html)                                                # 解析代码
    a = doc('.TypeList .TypeBigPics')
    for item in a.items():
        b = item.attr('href')              # 获得herf里的所有代码
    #    print(b,'\n','\n')
        html2 = requests.get(b,headers = headers,verify = False).text
        doc2 = pq(html2)
        c = doc2('.ImageBody img')         # 获得ImageBody img里的代码
        for item2 in c.items():
          d = item2.attr('src')            # 获得src里的链接
          print(d)

# 保存文件
          root = "new"   # 根目录
          path=root+d.split('/')[-1]
          # 根目录加上url中以反斜杠分割的最后一部分，即可以以图片原来的名字存储在本地

          print(root)
          try:
              if not os.path.exists(root):    # 判断当前根目录是否存在
                  os.mkdir(root)              # 创建根目录
              if not os.path.exists(path):    # 判断文件是否存在
                  r=requests.get(d)
                  with open(path,'wb')as f:
                      f.write(r.content)
                      f.close()
                      print("文件保存成功",'\n')
              else:
                  print("文件已存在")
          except:
              print("爬取失败")


# 控制代码运行过程，在文件作为脚本时才会被执行，而import到其他脚本中是不会被执行的
if __name__ == '__main__':
    z = 1
    url = 'http://www.umei.cc/p/gaoqing/cn/'     # 初始目标URL
    for i in range(z, z+1):                      # z+1可以换成z+n (n=1,2,3......)
        url1 = url+str(i)+'.htm'
        print(url1)
        get_url1(url1)                           # 调用get_url1函数获取图片
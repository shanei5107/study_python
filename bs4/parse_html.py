# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup

html_doc = """
<html><head><title>"c语言中文网"</title></head>
<body>
<p class="title"><b>c.biancheng.net</b></p>
<p class="website">一个学习编程的网站
<a href="http://c.biancheng.net/python/" id="link1">python教程</a>
<a href="http://c.biancheng.net/c/" id="link2">c语言教程</a>
"""
soup = BeautifulSoup(html_doc, 'html.parser')
print(soup.prettify())
print(soup.title)
print(soup.title.string)
print(soup.p)
print(soup.p['class'])
print(soup.a)
print(soup.find_all('a'))

for link in soup.find_all('a'):
    print(link.get('href'))

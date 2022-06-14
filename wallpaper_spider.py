# -*- coding: utf-8 -*-

import random
import re
from time import time
from urllib import parse
import requests
from fake_useragent import UserAgent


class WallpaperSpider(object):

    def __init__(self):
        self.params = {
            'categories': 110,
            'purity': 100,
            'atleast': '3840x2160',
            'sorting': 'random',
            'order': 'desc',
            'seed': 'N3JlwR',
        }
        self.url = 'https://wallhaven.cc/search?categories=110&purity=100&atleast=3840x2160&sorting=random&order=desc&seed=N3JlwR&page={}'
        # 计数，请求一个页面的次数，初始值为1
        self.blog = 1

    def get_header(self):
        '''
        随机获取请求头
        '''
        ua = UserAgent()
        headers = {'User-Agent': ua.random}
        return headers

    def get_html(self, url):
        '''
        请求获取网页信息
        '''
        if self.blog <= 3:
            try:
                res = requests.get(url=url,
                                   headers=self.get_header(),
                                   timeout=3)
                html = res.text
                return html
            except Exception as e:
                print(e)
                self.blog += 1
                self.get_html(url)

    def parse_html(self, url):
        '''
        解析提取数据
        '''
        html = self.get_html(url)
        print(html)
        if html:
            pass

    def run(self):
        '''
        入口函数
        '''
        try:
            for i in range(1, 2):
                url = self.url.format(i)
                self.parse_html(url)
                # time.sleep(random.randint(1, 3))
                # self.blog = 1
        except Exception as e:
            print('发生错误', e)


'''
壁纸
https://wallhaven.cc/search?categories=110&purity=100&atleast=3840x2160
&sorting=random&order=desc&seed=N3JlwR&page=2
'''
if __name__ == '__main__':
    spider = WallpaperSpider()
    spider.run()

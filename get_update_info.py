# coding=utf-8

import sys
import traceback
import random
from datetime import datetime

import requests
from bs4 import BeautifulSoup

from content_parsing import PageParsingTool

reload(sys)
sys.setdefaultencoding("utf-8")


class HostsPageCrawler():
    def __init__(self):
        self.user_agents = [
            'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 '
            'Mobile/13B143 Safari/601.1]',
            'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) '
            'Chrome/48.0.2564.23 Mobile Safari/537.36',
            'Mozilla/5.0 (Linux; Android 5.1.1; Nexus 6 Build/LYZ28E) AppleWebKit/537.36 (KHTML, like Gecko) '
            'Chrome/48.0.2564.23 Mobile Safari/537.36']
        self.headers = {
            'User_Agent': random.choice(self.user_agents),
            'Referer': 'https://laod.cn/hosts/2016-google-hosts.html'}
        self.login_url = 'https://laod.cn/hosts/2017-google-hosts.html'
        self.session = requests.session()

    def log_in(self):
        response = self.session.post(self.login_url, headers=self.headers)
        if response.status_code == 200:
            print u"获取页面成功：" + self.login_url
        else:
            raise Exception(u"获取页面失败")

    def get_page(self):
        page = self.session.get(self.login_url)
        return page.content

    def get_update_date(self):
        page = self.get_page()
        parsing_tool = PageParsingTool()
        title = parsing_tool.get_title(page)
        _date = parsing_tool.extra_update_date(title)
        if _date != 'Null':
            return datetime.strptime(_date, '%Y-%m-%d')
        else:
            return 'Null'

if __name__ == '__main__':
    host_page_crawler = HostsPageCrawler()
    host_page_crawler.log_in()
    print host_page_crawler.get_update_date()

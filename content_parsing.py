# coding=utf-8

import sys
import traceback
import re
from datetime import datetime

from bs4 import BeautifulSoup

reload(sys)
sys.setdefaultencoding("utf-8")



class PageParsingTool():
    def get_title(self, raw_page):
        soup = BeautifulSoup(raw_page, 'lxml')
        page = soup.prettify()
        return soup.title.string

    def extra_update_date(self, title_text):
        pattern = re.compile(u':(.*?)】', re.S)
        print title_text
        result = re.search(pattern, title_text)
        if result:
            return result.group(1)
        else:
            return 'Null'

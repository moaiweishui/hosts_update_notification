# coding=utf-8

import sys
from datetime import datetime, timedelta

from get_update_info import HostsPageCrawler
from push_update_info import send_email
reload(sys)
sys.setdefaultencoding("utf-8")


if __name__ == '__main__':
    hosts_page_crawler = HostsPageCrawler()
    hosts_page_crawler.log_in()
    update_date = hosts_page_crawler.get_update_date()
    # update_date = datetime.strptime('2017-08-11', '%Y-%m-%d')
    if update_date != 'Null':
        current_date = datetime.now()
        delta = current_date - update_date
        if delta.days == 1:
            send_email()
    else:
        print 'Extra update date failed'

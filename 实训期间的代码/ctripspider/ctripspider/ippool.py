import csv
import random

from lxml import etree
import requests
from redis import Redis


def check_url(key):
    index=key.find(':')
    proxy={
        key[:index]: key[index + 1:]
    }
    response1=requests.get(url='https://www.baidu.com',headers=headers,proxies=proxy)
    if response1.status_code==200:
        return True
    else:
        return False

def to_redis():
    for i in range(1,6):
        response=requests.get(url=base_url.format(i),headers=headers)
        html_str=response.text
        etreeobj=etree.HTML(html_str)
        tr_list=etreeobj.xpath('//table/tr')
        for tr in tr_list[1:]:
            ip=tr.xpath('./td[2]/text()')[0]
            port=tr.xpath('./td[3]/text()')[0]
            style = tr.xpath('./td[6]/text()')[0]
            key=style+'://'+ip+':'+port
            if check_url(key):
                res.set(key,port)
def get_ip():
    res = Redis(host='127.0.0.1', port=6379, db=10)
    ip=random.choice(res.keys())
    return ip

if __name__ == '__main__':
    base_url = 'http://www.xicidaili.com/nn/{}'
    res = Redis(host='127.0.0.1', port=6379, db=10)
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36",
    }





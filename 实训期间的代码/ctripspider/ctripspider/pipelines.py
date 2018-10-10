# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

import pymysql
from scrapy.utils.project import get_project_settings


class CtripspiderPipeline(object):
    def __init__(self):
        self.fp=open('ctrip.txt','a',encoding='utf-8')

    def process_item(self, item, spider):
        self.fp.write(json.dumps(dict(item),ensure_ascii=False)+'\n')


        return item
    def close_spider(self,spider):
        self.fp.close()


class CtripspiderMysqlPipeline:
    def __init__(self):
        settings=get_project_settings()
        self.con=pymysql.Connect(host=settings.get('MYSQL_HOST'),port=settings.get('MYSQL_PORT'),user=settings.get('MYSQL_USER'),password=settings.get('MYSQL_PASSWORD'),db=settings.get('MYSQL_DB'),charset=settings.get('MYSQL_CHARSET'))
        self.cursor=self.con.cursor()

    def process_item(self, item, spider):
        sql = 'insert into ctrip_strategy(author_name, title, write_time,travel_days,travel_mouth,travel_cost,strategy) values("%s", "%s", "%s", "%s", "%s", "%s", "%s")' % (item['author_name'], item['title'], item['write_time'], item['travel_days'], item['travel_mouth'], item['travel_cost'], item['strategy'])
        self.cursor.execute(sql)
        self.con.commit()
        return item

    def close_spider(self,spider):
        self.cursor.close()
        self.con.close()







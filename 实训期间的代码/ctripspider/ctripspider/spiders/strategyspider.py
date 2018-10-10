# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy_redis.spiders import RedisCrawlSpider
from ctripspider.items import CtripspiderItem

class StrategyspiderSpider(RedisCrawlSpider):
    name = 'strategyspider'
    # allowed_domains = ['ctrip.com']
    # start_urls = ['http://you.ctrip.com/place/hangzhou14.html']
    redis_key = 'start_url'

    rules = (
        Rule(LinkExtractor(restrict_xpaths='//div[@class="pager_v1"]/a[position()>1 and position()<7]'), callback='parse_item', follow=False),
    )

    def parse_item(self, response):

        url_list=response.xpath('//a[@class="journal-item cf"]/@href').extract()
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        for i in url_list:
            url='http://you.ctrip.com'+i
            yield scrapy.Request(url=url,callback=self.parse_detail)

    def parse_detail(self,response):
        item=CtripspiderItem()
        author_name=response.xpath('//p[@class="nickname"]/a/text()').extract_first(default='暂无作者')
        title=response.xpath('//h1/text()').extract_first(default='暂无攻略名')
        write_time=response.xpath('//div[@class="time"]/text()').extract_first(default='撰写时间未知')
        travel_days=response.xpath('//div[@class="bottom"]/span[1]/text()').extract_first(default='暂无旅行天数').split('：')[-1].strip()
        travel_mouth = response.xpath('//div[@class="bottom"]/span[2]/text()').extract_first(default='暂无旅行月份').split('：')[-1].strip()
        travel_cost= response.xpath('//div[@class="bottom"]/span[3]/text()').extract_first(default='暂无旅行花费').split('：')[-1].strip()
        strategy=''.join(response.xpath('//div[@class="ctd_content"]/p/text()').extract()).strip()
        item['author_name']=author_name
        item['title'] = title
        item['write_time'] = write_time
        item['travel_days'] = travel_days
        item['travel_mouth'] = travel_mouth
        item['travel_cost'] = travel_cost
        item['strategy'] = strategy
        yield item
# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TencentItem(scrapy.Item):
    # define the fields for your item here like:
    #职位名://div/table/tbody/tr/td/a/text()
    position_name = scrapy.Field()
    #职位类别://div/table/tbody/tr/td[2]/text()     [1:]
    position_type = scrapy.Field()
    #职位链接:https://hr.tencent.com/ + //div/table/tbody/tr/td/a/@href
    position_link = scrapy.Field()
    #招聘人数://div/table/tbody/tr/td[3]      [1:]
    position_num = scrapy.Field()
    #招聘地点：//div/table/tbody/tr/td[4]     [1:]
    position_location = scrapy.Field()
    #发布时间：//div/table/tbody/tr/td[5]     [1:]
    position_time = scrapy.Field()

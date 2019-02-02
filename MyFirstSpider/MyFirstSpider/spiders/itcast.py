# -*- coding: utf-8 -*-
import scrapy
from MyFirstSpider.items import MyfirstspiderItem

class ItcastSpider(scrapy.Spider):
    #爬虫名
    name = 'itcast'
    #爬虫作用的范围
    allowed_domains = ['http://www.itcast.cn/']
    #爬虫起始的url
    start_urls = [
        "http://www.itcast.cn/channel/teacher.shtml#aandroid",
        "http://www.itcast.cn/channel/teacher.shtml#ac",
        "http://www.itcast.cn/channel/teacher.shtml#acloud",
        "http://www.itcast.cn/channel/teacher.shtml#aios",
        "http://www.itcast.cn/channel/teacher.shtml#ajavaee",
        "http://www.itcast.cn/channel/teacher.shtml#anetmarket",
        "http://www.itcast.cn/channel/teacher.shtml#aphp",
        "http://www.itcast.cn/channel/teacher.shtml#apython",
        "http://www.itcast.cn/channel/teacher.shtml#astack",
        "http://www.itcast.cn/channel/teacher.shtml#aui",
        "http://www.itcast.cn/channel/teacher.shtml#aweb"
    ]

    def parse(self, response):
        #with open("itcast.html","w") as f:
        #    f.write(str(response.body))
        #teacher_item = []
        # extract() 将匹配出来的结果转换为Unicode字符串
        # 不加extract() 结果为xpath匹配对象
        name_list = response.xpath("//div/ul/li/div/h3/text()").extract()
        title_list = response.xpath("//div/ul/li/div/h4/text()").extract()
        info_list = response.xpath("//div/ul/li/div/p/text()").extract()
        for name,title,info in zip(name_list,title_list,info_list):
            item = MyfirstspiderItem()
            #print(name,title,info)
            item["name"] = name
            item["title"] = title
            item["info"] = info
            #teacher_item.append(item)
            yield item

        #return teacher_item

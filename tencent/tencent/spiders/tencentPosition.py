# -*- coding: utf-8 -*-
import scrapy
from tencent.items import TencentItem

class TencentpositionSpider(scrapy.Spider):
    name = 'tencent'
    allowed_domains = ['tencent.com']
    url = "https://hr.tencent.com/position.php?keywords=&tid=0&lid=2218&start="
    pg = 0
    start_urls = [url + str(pg)]

    def parse(self, response):
        #//div/table/tbody/tr
        for each in response.xpath("//tr[@class='even'] | //tr[@class='odd']"):
            item = TencentItem()
            # 职位名://div/table/tbody/tr/td/a/text()
            item["position_name"] = each.xpath("./td/a/text()").extract()
            # 职位类别://div/table/tbody/tr/td[2]/text()     [1:]
            item['position_type'] = each.xpath("./td[2]/text()").extract()
            # 职位链接:https://hr.tencent.com/ + //div/table/tbody/tr/td/a/@href
            item['position_link'] = "https://hr.tencent.com/" + str(each.xpath("./td/a/@href").extract())
            # 招聘人数://div/table/tbody/tr/td[3]      [1:]
            item['position_num'] = each.xpath("./td[3]/text()").extract()
            # 招聘地点：//div/table/tbody/tr/td[4]     [1:]
            item['position_location'] = each.xpath("./td[4]/text()").extract()
            # 发布时间：//div/table/tbody/tr/td[5]     [1:]
            item['position_time'] = each.xpath("./td[5]/text()").extract()

            yield item

        if self.pg <=1900:
            self.pg += 10

        yield scrapy.Request(self.url+str(self.pg),callback = self.parse)
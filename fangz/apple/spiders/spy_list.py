# -*- coding: utf-8 -*-
# 
#
import scrapy

from apple.items import AppleItem as DmozItem
from scrapy.spiders import CrawlSpider, Rule
from bs4 import BeautifulSoup

class DmozSpider(CrawlSpider):
     name = "dmoz3"
     # area_code = ['1646','1639','5278']
     start_urls = [
                    # "http://esf.sz.fang.com/housing/89__1_0_0_0_1_0_0/",
                    # "http://esf.sz.fang.com/housing/90__1_0_0_0_1_0_0/",
                    "http://esf.sz.fang.com/housing/87__1_0_0_0_1_0_0/",
                    # "http://esf.sz.fang.com/housing/85__1_0_0_0_1_0_0/",
                    # "http://esf.sz.fang.com/housing/86__1_0_0_0_1_0_0/",
                    # "http://esf.sz.fang.com/housing/88__1_0_0_0_1_0_0/",
                    # "http://esf.sz.fang.com/housing/13080__1_0_0_0_1_0_0/",
                    # "http://esf.sz.fang.com/housing/13079__1_0_0_0_1_0_0/",
                    # "http://esf.sz.fang.com/housing/13081__1_0_0_0_1_0_0/",
                    # "http://esf.sz.fang.com/housing/13082__1_0_0_0_1_0_0/",
                    # "http://esf.sz.fang.com/housing/13058__1_0_0_0_1_0_0/",
                    # "http://esf.sz.fang.com/housing/13057__1_0_0_0_1_0_0/",
                    # "http://esf.sz.fang.com/housing/16375__1_0_0_0_1_0_0/",

     ]

     def parse(self, response): #http://esf.sh.fang.com/housing/_5255_1_0_0_0_1_0_0/
          for sel in response.xpath('//div[@class="houseList"]/div'):   
                                   # /html/body/div[4]/div[5]/div[4]/div
               item = DmozItem()
               item['name'] = sel.xpath('dl/dd/p[1]/a/text()').extract()
               # item['price'] = sel.xpath('div/p[1]/span[1]/text()').extract()[0]
               item['resd1'] = sel.xpath('dl/dd/p[1]/a/@href').extract()
               yield item
               page_links=response.xpath('//*[@id="houselist_B14_01"]/a/text()').extract()
               for link in page_links:
                    if u'下一页' in link:
                         next_link = response.xpath('//*[@id="houselist_B14_01"]/a/@href').extract()[-2]
                         next_link="http://esf.sz.fang.com" + next_link
                         yield scrapy.Request(next_link, callback=self.parse)
          



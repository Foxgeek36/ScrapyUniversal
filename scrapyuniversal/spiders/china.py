# -*- coding: utf-8 -*-
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapyuniversal.items import *
from scrapyuniversal.loaders import *

'''
[state]使用通用爬虫标准模块爬取->https://tech.china.com/articles/
'''


class ChinaSpider(CrawlSpider):
    name = 'china'
    allowed_domains = ['tech.china.com']
    # 根据目标页面做自定义设置
    start_urls = ['http://tech.china.com/articles/']
    
    rules = (
        # 获取当前所在列表页数据
        Rule(LinkExtractor(allow='article\/.*\.html',
                           restrict_xpaths='//div[@id="left_side"]//div[@class="con_item"]'),
                           callback='parse_item'),
        # 获取'下一页'列表页
        Rule(LinkExtractor(restrict_xpaths='//div[@id="pageStyle"]//a[contains(., "下一页")]'))
    )

    # 此处的方法区别于原有的 parse()
    def parse_item(self, response):
        loader = ChinaLoader(item=NewsItem(), response=response)
        loader.add_xpath('title', '//h1[@id="chan_newsTitle"]/text()')
        loader.add_value('url', response.url)
        loader.add_xpath('text', '//div[@id="chan_newsDetail"]//text()')
        loader.add_xpath('datetime', '//div[@id="chan_newsInfo"]/text()', re='(\d+-\d+-\d+\s\d+:\d+:\d+)')
        loader.add_xpath('source', '//div[@id="chan_newsInfo"]/text()', re='来源：(.*)')
        loader.add_value('website', '中华网')
        yield loader.load_item()

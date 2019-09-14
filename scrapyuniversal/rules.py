# coding=utf-8
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule

'''
# 对应json文件中的'rules'字段/ 做抽离单独设置的rules.py,做成配置文件,实现Rule的分离
'''


rules = {
    'china': (
        Rule(LinkExtractor(allow='article\/.*\.html', restrict_xpaths='//div[@id="left_side"]//div[@class="con_item"]'),
             callback='parse_item'),
        Rule(LinkExtractor(restrict_xpaths='//div[@id="pageStyle"]//a[contains(., "下一页")]'))
    )
}

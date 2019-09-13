# coding=utf-8
import sys
from scrapy.utils.project import get_project_settings
from scrapyuniversal.spiders.universal import UniversalSpider
from scrapyuniversal.utils import get_config
from scrapy.crawler import CrawlerProcess


def run():
    '''
    为入口文件,作用是启动Spider/ 添加该文件之后,项目的启动命令为python run.py china
    '''
    name = sys.argv[1]  # 获取cmd命令行中的指令参数
    custom_settings = get_config(name)
    # 爬虫执行的spider名称
    spider = custom_settings.get('spider', 'universal')
    project_settings = get_project_settings()
    settings = dict(project_settings.copy())
    # 合并所有配置
    settings.update(custom_settings.get('settings'))
    process = CrawlerProcess(settings)
    # 启动爬虫
    process.crawl(spider, **{'name': name})
    process.start()


if __name__ == '__main__':
    run()

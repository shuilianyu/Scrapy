# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


class MultiscrapySpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class MultiscrapyDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


import time
from scrapy.http import HtmlResponse


class SeleniumMiddlewares(object):
    '''
    Selenium,用来使用模拟器模拟下载请求,注意打开DOWNLOADER_MIDDLEWARES
    '''

    def __init__(self):
        '''
        初始化一个FireFox实例
        '''
        self.options = Options()
        self.options.add_argument('-headless')
        self.browers = webdriver.Firefox(executable_path='/home/yangfubo/geckodriver', firefox_options=self.options)

    def process_request(self, request, spider):
        '''
        该方法在中间件被激活的时候系统自动调用,处理request请求
        spider.name可以区分不同爬虫
        :param request:
        :param spider:
        :return:
        '''
        # 使用元数据meta中的page判断是否是翻页请求
        if not request.meta["is_first_page"] and request.meta['to_next_page']:
            # 将页面滚动到最后
            self.browers.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            # #找到下一页并模拟点击
            time.sleep(4)
            btn = self.browers.find_element_by_xpath('//div[@class="pager"]/button[2]')
            btn.click()
            time.sleep(3)
            return HtmlResponse(url=self.browers.current_url, body=self.browers.page_source, encoding='utf-8',
                                request=request)

        else:
            if request.meta["is_first_page"]:
                # 将页面滚动到最后
                self.browers.get(request.url)
                return HtmlResponse(url=request.url, body=self.browers.page_source, encoding='utf-8',request=request)
            else:
                pass
            # print('已经翻页了')
            # 生成HTMLResponse,将浏览器模拟的下载结果返回给我们的spider,结果存在self.browers.page_source中
            # 结果是整个页面的html代码


import random

PROXIES = []


class ProxyMiddleware(object):

    def process_request(self, request, spider):
        ip = random.choice(PROXIES)
        request.meta['proxy'] = ip

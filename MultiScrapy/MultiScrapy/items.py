# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MultiscrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class JobItem(scrapy.Item):
    '''
    定义数据模型类,需要打开ITEM_PIPELINES
    '''
    job_title = scrapy.Field()
    job_categories = scrapy.Field()
    wage = scrapy.Field()
    location = scrapy.Field()
    work_experience = scrapy.Field()
    education = scrapy.Field()
    recruits_number = scrapy.Field()
    company_name = scrapy.Field()
    company_type = scrapy.Field()
    company_size = scrapy.Field()
    company_address = scrapy.Field()
    job_description = scrapy.Field()
    welfare_pos = scrapy.Field()

# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import sqlite3
class MultiscrapyPipeline(object):
    '''
    处理spider解析过的item结果,可以存入数据库或文件,需要打开ITEM_PIPELINES才能生效
    '''
    def __init__(self):
        self.coon = sqlite3.connect("zhilianzhaopin.db")
        self.cursor = self.coon.cursor()
    def process_item(self, item, spider):
        try:
            self.cursor.execute('create table jobs (id INTEGER PRIMARY KEY AUTOINCREMENT,job_title varchar(20),job_categories varchar(20),wage varchar(15),location varchar(25),work_experience varchar(10),education varchar(10),recruits_number varchar(10),company_name varchar(20),company_type varchar(10),company_size varchar(10),company_address varchar(15), welfare_pos message_text,job_description message_text )')
        except:
            pass
        #防止抓取内容中出现和sql关键字冲突
        # sql_insert = '''insert into country values (?,?)'''
        # param = (item['name'],item['population'])
        # self.cursor.execute(sql_insert,param)
        self.cursor.execute("insert into jobs(job_title,job_categories,wage,location,work_experience,education,recruits_number,company_name,company_type,company_size,company_address,welfare_pos,job_description) values('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}') ".format(item['job_title'],item["job_categories"],item["wage"],item["location"],item["work_experience"],item["education"],item["recruits_number"],item["company_name"],item["company_type"],item["company_size"],item["company_address"],item["welfare_pos"],item["job_description"]))
        self.coon.commit()

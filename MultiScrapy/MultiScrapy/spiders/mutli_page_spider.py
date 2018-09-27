from scrapy import Spider
from scrapy import Request
import time
import lxml.html
from MultiScrapy.items import JobItem
from collections import Counter

class JobProfile(object):
    '''
    工作描述类,模型类,用来存储解析结果,及进行一些简单的数据清洗(筛选)
    '''
    def __init__(self):
        self.job_title = ''
        self.job_url = ''
        self.saray = ''
        self.location = ''
        self.saray_range = [5000,20000]

        self.aera_range =[ '郑州','上海','北京','深圳','广州','天津','成都','杭州','武汉'
        ,'大连','长春','南京','济南','青岛','苏州','沈阳','西安',
        '长沙','重庆','哈尔滨','无锡','宁波','福州','厦门','石家庄','合肥','惠州']
    #限制薪资待遇
    def salary_limit(self):
        return True
        # try:
        #     min_wage = float(self.saray.split('-', 1)[0])
        #     max_wage = float(self.saray.split('-', 1)[1])
        # except:
        #     return False
        # else:
        #     if min_wage >= self.saray_range[0] and max_wage <= self.saray_range[1]:
        #         return True
        #     else:
        #         return False
    #限制地区
    def aera_limit(self):
        # return True
        return self.location.split('-',1)[0] in self.aera_range

    #限制行业python
    def job_limit(self):
        return self.job_title in ['Python','python']



def time_url():
    return 'http://www.baidu.com{}/'.format(round(time.time()*1000))

def judge_next_page_exist(response):
    try:
        btn = response.xpath('//button[@class="btn btn-pager btn-pager-disable"]/text()').extract()[0]
        print(btn)
    except:
        return True
    else:
        if btn=='下一页':
            return False
        elif btn=='上一页':
            try:
                response.xpath('//button[@class="btn btn-pager btn-pager-disable"]/text()').extract()[1]
            except:
                return True
            else:
                return False
        else:
            return True



class MultiPageSpider(Spider):
    '''
    多页爬取,用于爬去当前页,及递归爬取下一页的内容
    对于没有下一页按钮的,查找其他翻页方法
    '''
    def __init__(self):
        super().__init__()
        self.list=[719,538,530,765,763,531,801,653,736,600,613,635,702,703,639,599,854,749,551,622,636,654,681,682,565,664,773]

    name = "multi_page_spider"#爬虫名称

    def start_requests(self):
        '''
        1.引擎启动调用函数,该函数第一个要下载的网址,通过返回的Request对象实现
        该方法和start_urls属性提供的方法相同,选用其一即可
        2.如果选用start_urls默认解析方法是parse,不能顺便写
        :return:
        '''
        #719郑州538上海530北京765深圳763广州#天津531成都801#杭州653#武汉736
        #大连600#长春613#南京635#济南702#青岛703#苏州639#沈阳599#西安854
        #长沙749#重庆551#哈尔滨622#无锡636#宁波654#福州681#厦门682#石家庄565#合肥664#惠州773
        #全国489

        url_str = "https://sou.zhaopin.com/?pageSize=60&jl={}&kw=python&kt=3".format(489)
        #Request提供下载请求,下载成功后系统会自动调用callback方法向用户返回下载结果
        #meta用于指定附加的用户元数据,可以随意指定需要的键值对,该元数据在整个request,response的生命周期都会被携带
        yield Request(url=url_str,callback=self.parse,meta={'to_next_page':False,'is_first_page':True})

    def parse(self, response):
        # 使用页面xpath选择器
        print(response.url)
        jobs = response.xpath('//div[@class="listItemBox-wrapper clearfix"]').extract()
        # # page_index = response.css('button.btn:nth-child(8)').extract()
        for job in jobs:
            #解析一条工作的详细信息,该工作内容位于一条嵌套的html中
            #所以另外使用一个函数解析
            job_profile = self.parse_one_job(job)
            if not job_profile.aera_limit():
                #下载一条工作的详细信息,地址在parse_one_job解析
                #下载成功后会调用parse_detail
                yield Request(url=job_profile.job_url,callback=self.parse_detail,meta={'to_next_page':False,'is_first_page':False})
        if judge_next_page_exist(response):
            print(response.url)
            print('我要取翻页')
            # 使用selenium模拟点击下一页,该请求不会产生实质的下载动作
            yield Request(url='http://www.baidu.com',dont_filter=True,callback=self.parse,meta={'to_next_page':True,'is_first_page':False})


    def parse_detail(self,response):
        '''
        用于解析工作详细信息,将结果封装为指定的Item,送到pipeline,进一步存入数据库
        :param response:
        :return:
        '''
        job_categories_old = ''.join(response.xpath('//ul[@class="terminal-ul clearfix"]/li[8]/strong/a/text()').extract())
        job_categories_new = ''.join(response.xpath('//h1[@class="l info-h3"]/text()').extract())
        job_title = ''.join(response.xpath('//h1/text()').extract())
        if job_categories_old:
            job_categories = job_categories_old
            location = ''.join(response.xpath('//ul[@class="terminal-ul clearfix"]/li[2]/strong/a/text()').extract())
            wage = ''.join(response.xpath('//ul[@class="terminal-ul clearfix"]/li[1]/strong/text()').extract()).rstrip('\xa0')
            work_experience = ''.join(response.xpath('//ul[@class="terminal-ul clearfix"]/li[5]/strong/text()').extract())
            education = ''.join(response.xpath('//ul[@class="terminal-ul clearfix"]/li[6]/strong/text()').extract())
            recruits_number = ''.join(response.xpath('//ul[@class="terminal-ul clearfix"]/li[7]/strong/text()').extract())
            company_name = ''.join(response.xpath('//p[@class="company-name-t"]/a/text()').extract())
            company_type = ''.join(
                response.xpath('//ul[@class="terminal-ul clearfix terminal-company mt20"]/li[2]/strong/text()').extract())
            company_size = ''.join(
                response.xpath('//ul[@class="terminal-ul clearfix terminal-company mt20"]/li[1]/strong/text()').extract())
            company_address = ''.join(
                response.xpath('//ul[@class="terminal-ul clearfix terminal-company mt20"]/li[last()]/strong/text()').extract()).strip()
            job_description_base = response.xpath('//div[@class="tab-inner-cont"][1]')
            job_description = ''.join(job_description_base.xpath('string(.)').extract())
            # job_description_div = ' '.join(response.xpath('//div[@class="tab-inner-cont"][1]/div/text()').extract()).strip()
            # job_description_p_span = ' '.join(response.xpath('//div[@class="tab-inner-cont"][1]/p/span/text()').extract()).strip()
            # job_description = job_description_p_span + job_description_div + job_description_p
            welfare_pos = ','.join(response.xpath('//div[@class="welfare-tab-box"]/span/text()').extract())

        else:
            job_categories = job_categories_new
            wage = ''.join(response.xpath('//div[@class="l info-money"]/strong/text()').extract())
            location = ''.join(response.xpath('//div[@class="info-three l"]/span[1]/a/text()').extract())
            work_experience = ''.join(response.xpath('//div[@class="info-three l"]/span[2]/text()').extract())
            education = ''.join(response.xpath('//div[@class="info-three l"]/span[3]/text()').extract())
            recruits_number = ''.join(response.xpath('//div[@class="info-three l"]/span[4]/text()').extract())
            company_name = ''.join(response.xpath('//h3/a/text()').extract())
            company_type = ''.join(response.xpath('//ul[@class="promulgator-ul cl"]/li[2]/strong/text()').extract())
            company_size = ''.join(response.xpath('//ul[@class="promulgator-ul cl"]/li[3]/strong/text()').extract())
            company_address = ''.join(response.xpath('//ul[@class="promulgator-ul cl"]/li[last()]/strong/text()').extract())
            # company_address_2=''.join(response.xpath('//ul[@class="promulgator-ul cl"]/li[5]/strong/text()').extract())
            job_description_base = response.xpath('//div[@class="responsibility pos-common"]/')
            job_description = ''.join(job_description_base[0].xpath('string(.)').extract())

            # job_description_div_div = ''.join(
            #     response.xpath('//div[@class="responsibility pos-common"]/div/div/text()').extract())
            # job_description_div = ''.join(
            #     response.xpath('//div[@class="responsibility pos-common"]/div/div/p/span/text()').extract())
            # job_description_p_span = ''.join(response.xpath('//div[@class="responsibility pos-common"]/div/p/span/text()').extract())
            # job_description = job_description_p+job_description_div+job_description_p_span+job_description_div_div
            welfare_pos = ','.join(response.xpath('//div[@class="welfare"]/ul/li/text()').extract())
        if Counter([job_title,job_categories,location,wage,work_experience,education,recruits_number,company_address,company_size,company_type,company_name,job_description,welfare_pos])['']<=10:
            item = JobItem()
            item['job_title'] = job_title
            item['job_categories']= job_categories
            item['location'] = location
            item['wage'] = wage
            item['work_experience'] = work_experience
            item['education'] = education
            item['recruits_number'] = recruits_number
            item['company_name'] = company_name
            item['company_size'] = company_size
            item['company_type'] = company_type
            item['company_address'] = company_address
            item['job_description'] = job_description
            item['welfare_pos'] = welfare_pos
            yield item
        else:
            pass


    def parse_one_job(self,html_str):
        '''
        根据内部html解析工作详细内容,包括,公司名薪水地区职位等
        :param html_str:
        :return:
        '''
        job_profile = JobProfile()
        tree_xml = lxml.html.fromstring(html_str)
        # job_title = tree_xml.xpath('//span[@class="job_title"]/text()')
        #获取详细内容网址,xpath返回的是数组
        try:
            job_profile.job_url = tree_xml.xpath('//div[@class="jobName"]/a/@href')[0]
            job_profile.saray = tree_xml.xpath('//p[@class="job_saray"]/text()')[0]
            job_profile.location = tree_xml.xpath('//ul[@class="job_demand"]/li[1]/text()')[0]
            job_profile.job_title = tree_xml.xpath('//div[@class="jobName"]/a/span/span')[0]
        except:
            pass
        return job_profile


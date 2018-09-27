# Scrapy

A Zhilian Recruiting Reptile Project

#本项目用于抓取智联招聘网站上有关python职位的相关信息,也可以按照指定的城市抓取

#使用了selenium模拟以scrapy框架,巧妙的解决了使用ajax请求的页面与翻页问题

#使用scrapy框架时发现抓取的是老版的智联招聘网站,于是抓取工作详细信息时要使用老版页面进行匹配

#本项目可供参考无法抓取ajax请求页面,与无法翻页的问题



项目运行(项目中已经存在抓取后的数据库,如果想重新抓取,可删除它,或更改连接数据库的名字)

1.安装环境,本项目所需的环境已生成requirements.txt

  可pip install -r requirements.txt直接导入
  
2.运行

  在爬虫文件中选择城市(在url_str中输入城市对应的标号)
  
  使用scrapy crawl multi_page_spider(爬虫的名字)
  
 更多详情,请自己领悟
 

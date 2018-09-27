# # from selenium.webdriver.common.action_chains import ActionChains
# # from selenium.webdriver.firefox.options import Options as FOptions
# # from selenium import webdriver
# # import time
# #
# # options = FOptions()
# # options.add_argument('-headless')
# # borwser = webdriver.Firefox(
# #     executable_path='/home/yangfubo/geckodriver',
# #     firefox_options=options
# # )
# # borwser.implicitly_wait(2)
# # borwser.maximize_window()
# # borwser.get('https://sou.zhaopin.com/jobs/searchresult.ashx?jl=489&kw=python&sm=0&p=1')
# # time.sleep(1)
# # btn1 = borwser.find_element_by_link_text('返回旧版')
# # btn1.click()
# # key_words = borwser.find_element_by_xpath('//input[@id="KeyWord_kw2"]')
# # key_words.send_keys('python')
# # btn_key_word = borwser.find_element_by_xpath('//button[@class="doesSearch"]')
# # btn_key_word.click()
# # jobs = borwser.find_elements_by_xpath('//table[@class="newlist"]')
# #
# # print(jobs)
# s='''
#
#                     '<table class="newlist" width="853" cellspacing="0" cellpadding="0">\n                            <tbody><tr>\n                                <td class="zwmc" style="width: 250px;">\n                                    <input name="vacancyid" data-monitor="CC566985188J90251735000|60" value="CC566985188J90251735000_763_1_03_201__1_" onclick="zlapply.uncheckAll(\'allvacancyid\')" type="checkbox">\n                                    <div style="width: 224px;*width: 218px; _width:200px; float: left">\n                                        <a style="font-weight: bold" par="ssidkey=y&amp;ss=201&amp;ff=03&amp;sg=5e10fc6076114d2288e36b2f8927a960&amp;so=60" href="http://jobs.zhaopin.com/566985188251735.htm" target="_blank">急招初级<b>Python</b>开发/双休年底双薪</a>\n                                /div>\n                                </td>\n                                <td style="width: 60px; color: red;" class="fk_lv"><span>99%</span></td>\n                                <td class="gsmc"><a href="http://company.zhaopin.com/CZ566985180.htm" target="_blank">广州动点网络科技有限公司</a> <a href="http://company.zhao6985180.htm" target="_blank" style="vertical-align: top;"><img src="//img03.zhaopin.cn/IHRNB/img/souvip1003.png" alt="1003" class="icon_vip" border="0" align="absmiddle"></a></td>\n                                <td class="zwyx">4001-6000</td>\n                                <td class="gzdd">广州-海珠区</td>\n                           <td class="gxsj"><span>最新</span><a class="newlist_list_xlbtn" href="javascript:;"></a></td>\n                          </tr>\n                            <tr style="display: none" class="newlist_tr_detail">\n                                <td style="line-height: 0;" colspan="6" width="833px">\n                                    <div class="newlist_detail">\n                                        <div class="clearfix">\n                                            <ul>\n                                                <li class="newlist_deatil_two"><span>地点：广州-海珠区</span><span>公司性质：民营</span><span>公司规模：100-499人</n><span>职位月薪：4001-6000元/月</span></li><li class="newlist_deatil_last">  岗位职责：  1、录入网站站点；  码；  3、其他领导交给的任务；  4、负责物联网应用系统开发、算法实现。   任职要求：  1.计算机科学、软件工程相关语 言；  3.了解linu...</li>\n                                                \n                                       </ul>\n                                            <dl>\n                                                <dt>\n                                                    <a href="javascript:zlapply.searchjob.ajaxApplyBrig1(\'CC566985188J90251735000_763\',\'ssi\',\'_1_03_201__2_\');searchMonitor.logSingleApplyData(\'CC566985188J90251735000%7C60\');">\n                                                        <img src="/assets/images/newlist_sqimg_03.jpg">\n                                                    </a>\n                                                </dt>\n                                                <dd><a href="javascript:zlapply.searchjob.saveOne(\'CC566985188J90251735000_763\');"><img src="/assets/images/newlist_scimg_06.jpg"></a></dd>\n                                            </dl>\n                                        </div>\n                                    </div>\n                            </td></tr>\n                        </tbody></table>'
# '''
# print('https://sou.zhaopin.com/jobs/searchresult.ashx?jl=%e5%85%a8%e5%9b%bd&kw=python&sm=0&sg=a289003e8d4b4cbba5b80cd42808a685&p=' in 'https://sou.zhaopin.com/jobs/searchresult.ashx?jl=%e5%85%a8%e5%9b%bd&kw=python&sm=0&sg=a289003e8d4b4cbba5b80cd42808a685&p')
# # print('' in ['a','aaa'])
# from collections import Counter
# print(Counter(['','','','a'])[''])
print('sss' not in 'aaass')
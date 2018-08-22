# -*- coding: utf-8 -*-
import scrapy
import csv
from copy import deepcopy

class AnecdotespiderSpider(scrapy.Spider):
    name = 'AnecdoteSpider'
    allowed_domains = ['qiushibaike.com']
    start_urls = ['http://qiushibaike.com/']

    def parse(self, response):
        """"""
        """开始爬取"""
        div_left= response.xpath("//div[@id='content-left']")
        print(type(div_left))
        print("*"*100)

        # 页码
        page = 1

        """1. 获取div_left中的所有div"""
        # 注意：返回的div_left是一个<selector>对象（一个包含字符串的列表）
        # ret1 = response.xpath("//div[@class='li_txt']/h3/text()")

        # (extract()是从选择器对象<selector>中提取包含字符串的特殊列表)
        # ret2.extract()

        # extract_first()相当于extract()[0]
        div_list = div_left.xpath("./div")
        print(len(div_list))
        for div in div_list:
            # print(div)
            # print()
            """2. 创建一个字典，用来存储数据"""
            item = {}
            # 用户名
            item["name"] = div.xpath(".//h2/text()").extract_first()\
                .replace("\n","")
            # 用户等级
            item["level"] = div.xpath(".//div[contains(@class,"
                                      "'articleGender')]/text()").extract_first()
            if item["level"] is None:
                item["level"] = "无等级的辣鸡"

            # 内容
            item["content"] = div.xpath(".//div[@class='content']"
                                        "/span[not(@class='contentForAll')]/text()")\
                                        .extract()
            if len(item["content"]) >= 1:
                item["content"] = [i.replace("\n","").replace("\r","")
                                   for i in item["content"]]

            # url地址
            item["url"] = "https://www.qiushibaike.com"+div.xpath(".//a[@class='contentHerf']/@href").extract_first()

            print(item)

            """3. 将数据传输至pipline"""
            yield item

            """4. 进入下一页爬取"""
            page += 1
            next_url = "https://www.qiushibaike.com/8hr/page/{}/".format(page)
            yield scrapy.Request(
                next_url,
                # 重复parse方法进行数据爬取！
                callback=self.parse
                # meta={"item":deepcopy(item)},
                # dont_filter=True
            )



































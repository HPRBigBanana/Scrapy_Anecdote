# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import csv
import numpy as np
import pandas as pd

"""引入the01_Scrapy_Anecdote项目下的 spiders文件夹中的 AnecdoteSpider模块中的
    AnecdotespiderSpider类"""
from the01_Scrapy_Anecdote.spiders.AnecdoteSpider import AnecdotespiderSpider

class The01ScrapyAnecdotePipeline(object):

    # value = 0

    def process_item(self, item, spider):
        """"""
        # 声明要采用的全局变量(无法使用？)

        """1. process_item(self, item, spider)中的item就是从spider传递过来的数据"""

        """2. 将数据保存至csv文件中"""
        item_tuple = tuple(item.values())
        print(item_tuple)

        with open("G:/Python_file/csv/Anecdote_糗事百科.csv", "a") as csvfile:
            writer = csv.writer(csvfile)

            # 注意：keys的值只显示一次
                # 先写入columns_name
                # writer.writerow(item.keys())
                # # a += 1

            # 写入多行用writerows
            writer.writerow(item_tuple)


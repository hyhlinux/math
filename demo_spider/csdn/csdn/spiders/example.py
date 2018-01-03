# -*- coding: utf-8 -*-
import os
import scrapy


class CsdnSpider(scrapy.Spider):
    name = 'csdn'
    allowed_domains = ['csdn.net']
    start_urls = ['https://www.csdn.net/']

    def parse(self, response):
        filename = os.path.join("/tmp/", response.url.split("/")[-2])
        print("filename:{}".format(filename))
        with open(filename, 'wb') as f:
            f.write(response.body)
        pass

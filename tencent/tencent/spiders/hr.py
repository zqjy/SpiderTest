# -*- coding: utf-8 -*-
import scrapy


class HrSpider(scrapy.Spider):
    name = "hr"
    allowed_domains = ["tencent.com"]
    start_urls = ['http://tencent.com/']

    def parse(self, response):
        pass

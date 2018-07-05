# -*- coding: utf-8 -*-
from lxml import etree

import scrapy
from scrapy import Selector

from ScrapyTest.items import ScrapytestItem


class BaikeSpider(scrapy.Spider):
    name = 'baike'
    # allowed_domains = ['www.hao6v.com']
    start_urls = ['http://www.hao6v.com/s/gf250/index.html', ]
    for i in range(1,12):
        url = 'http://www.hao6v.com/s/gf250/index_%d.html' %i
        start_urls.append(url)



    def parse(self, response):
        html = Selector(response)
        liss = html.xpath('//*[@id="main"]/div[1]/div/ul/li')

        for l in liss:
            titles = l.xpath('a/text()').extract()
            links = l.xpath('a/@href').extract()
            for link in links:
                yield scrapy.Request(link, callback=self.parse_item)

    def parse_item(self, response):
        item = ScrapytestItem()
        movie = Selector(response)
        movies = movie.xpath('//*[@id="endText"]/table/tbody').extract()
        titles = movie.xpath('//*[@id="main"]/div[1]/div/h1/text()').extract()
        item["movies"] = movies
        item["titles"] = titles
        yield item

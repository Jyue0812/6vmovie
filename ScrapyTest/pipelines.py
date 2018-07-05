# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class ScrapytestPipeline(object):
    def process_item(self, item, spider):
        with open('./top250.txt', 'a', encoding='utf-8') as f:
            titles = item['titles']
            movies = item['movies']
            for i, j in zip(titles, movies):
                f.write(i + ':' + j + '\n')
        return item

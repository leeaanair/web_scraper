# -*- coding: utf-8 -*-
import scrapy
class RedditbotSpider(scrapy.Spider):
    name = 'redditbot'
   # allowed_domains = ['www.quora.com']
    url=input("Insert URL")
    start_urls = [url]

    def parse(self, response):
        titles = response.css('.container::text').extract()
        #Give the extracted content row wise
        for item in zip(titles):
            #create a dictionary to store the scraped info
            scraped_info = {
                'title' : item[0],
            }

            #yield or give the scraped info to scrapy
            yield scraped_info



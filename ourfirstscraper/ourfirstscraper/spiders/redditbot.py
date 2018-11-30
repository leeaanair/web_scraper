# -*- coding: utf-8 -*-
import scrapy
class RedditbotSpider(scrapy.Spider):
	name = 'redditbot'
	url=input("Insert URL")
	start_urls = [url]
	def parse(self, response):
		titles = response.css('*::text').extract()
		for item in zip(titles):
			if(item[0]==''):
				pass	
			else:
				scraped_info = {'title' : item[0],}
			yield scraped_info


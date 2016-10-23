# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 21:18:24 2016

@author: Amine
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 19:59:40 2016

@author: Amine
"""

import scrapy

from deepki.items import InterieurItem

class deepkiSpider(scrapy.Spider):
    name = "deepki" 
    allowed_domains = ["immochan.com"] 
    start_urls = [
        "http://www.immochan.com/fr/implantations-sites-commerciaux",
    ]
    
    def parse(self, response):
        for url in response.xpath('//td[@class = "views-field views-field-title-field"]/a/@href').extract():
            yield scrapy.Request(url, callback=self.parse_site)
        
        next_page = response.xpath('//div[@class = "attachment attachment-after"]/div/div[2]/ul[@class = "pager clearfix"]/li[@class = "pager-next"]/a/@href').extract()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            print('\n \n \n')            
            print(next_page)
            print('\n \n \n')
            yield scrapy.Request(next_page, callback=self.parse)
       
 
        
    def parse_site(self, response):
        interieur = InterieurItem() 
        
        interieur['Site'] = response.xpath('//div[@class = "region-inner region-content-inner"]/h1/text()').extract()
        interieur['Ville'] = response.xpath('//div[@class = "block-inner clearfix"]/div/article/div[1]/div[1]/div/div/text()').extract()
        interieur['Statut'] = response.xpath('//div[@class = "block-inner clearfix"]/div/article/div[1]/div[2]/div/div/div/div/span/text()').extract()
        interieur['Surface_GLA'] =  response.xpath('//div[@class = "views-field views-field-field-shopping-center-surface"]/div/span[1]/text()').extract()
        interieur['Nb_boutiques'] =  response.xpath('//div[@class = "views-field views-field-field-number-of-shops"]/div/span[1]/text()').extract()        
        interieur['Surface_hyper'] =  response.xpath('//div[@class = "views-field views-field-field-superstore-space"]/div/span[1]/text()').extract()
        
        ll = len(response.xpath('//div[@class = "views-field views-field-field-surname-1"]/div/a/span[1]/text()').extract())
        if ll == 1 :
            u_prenom = response.xpath('//div[@class = "views-field views-field-field-surname-1"]/div/a/span[1]/text()').extract()[0]
            u_nom = response.xpath('//div[@class = "views-field views-field-field-surname-1"]/div/a/span[2]/text()').extract()[0]
            uu = u_prenom + ' ' + u_nom
            interieur['Contact'] = [uu]
        else:
            interieur['Contact'] = []
        
        
        interieur['Fonction'] =response.xpath('//div[@class = "views-field views-field-field-job"]/div/text()').extract()
        
        l = len(response.xpath('//div[@class = "views-field views-field-field-surname-1"]/div/a/@href').extract())
        if l == 1 :
            u = response.xpath('//div[@class = "views-field views-field-field-surname-1"]/div/a/@href').extract()[0]
            interieur['Mail'] = [u.split(":")[1]]
        else:
            interieur['Mail'] = response.xpath('//div[@class = "views-field views-field-field-surname-1"]/div/a/@href').extract()
        
        interieur['Telephone'] = response.xpath('//div[@class = "views-field views-field-field-phone-1"]/span[2]/text()').extract()
        interieur['Mobile'] = response.xpath('//div[@class = "views-field views-field-field-phone-2"]/span[2]/text()').extract()
        interieur['Mobile'] = response.xpath('//aside[@id = "region-sidebar-second"]/div/div[2]/div/div/div/div/div/div[4]/span[2]/text()').extract()
        yield(interieur)
        
        
            
 


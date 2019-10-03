# -*- coding: utf-8 -*-
import scrapy
from scraping_kolo_vysledky.items import ScrapingTabulkyTymy
from scrapy.loader import ItemLoader
import sys
import string


class ScrapeTymSpider(scrapy.Spider):
    name = 'tabulky'
    allowed_domains = ['www.fotbalpraha.cz']
    start_urls = [  "https://www.fotbalpraha.cz/souteze/tabulka/153-a2b-1-a-trida-skupina-b-muzu?id_season=2019",
                    "https://www.fotbalpraha.cz/souteze/tabulka/154-a3a-1-b-trida-skupina-a-muzu?id_season=2019",
                    "https://www.fotbalpraha.cz/souteze/tabulka/158-a4c-2-trida-skupina-c-muzu?id_season=2019",
                    "https://www.fotbalpraha.cz/souteze/tabulka/162-c2a-1-trida-starsiho-dorostu?id_season=2019",
                    "https://www.fotbalpraha.cz/souteze/tabulka/165-d4a-2-trida-mladsiho-dorostu?id_season=2019",
                    "https://www.fotbalpraha.cz/souteze/tabulka/168-e2b-1-trida-skupina-b-starsich-zaku?id_season=2019",
                    "https://www.fotbalpraha.cz/souteze/tabulka/171-f1a-prebor-mladsich-zaku?id_season=2019",
                    "https://www.fotbalpraha.cz/souteze/tabulka/173-f2b-1-trida-skupina-b-mladsich-zaku?id_season=2019",
                    "https://www.fotbalpraha.cz/souteze/tabulka/174-f3a-2-trida-skupina-a-mladsich-zaku?id_season=2019"]

    def parse(self, response):
            l=ItemLoader(item=ScrapingTabulkyTymy(), response=response)
            poradi_tymu=response.xpath('//div[@class="typography table-responsive"]/table').xpath('//td[1]/text()').extract()
            tym=response.xpath('//div[@class="typography table-responsive"]/table').xpath('//td[2]/div/a/span[@class="middle"]/text()').extract()
            pocet_utkani=response.xpath('//div[@class="typography table-responsive"]/table').xpath('//td[3]/text()').extract()
            kolo=pocet_utkani[0];
            pocet_vitezstvi=response.xpath('//div[@class="typography table-responsive"]/table').xpath('//td[4]/text()').extract()
            pocet_remiz=response.xpath('//div[@class="typography table-responsive"]/table').xpath('//td[5]/text()').extract()
            pocet_proher=response.xpath('//div[@class="typography table-responsive"]/table').xpath('//td[6]/text()').extract()
            skore=response.xpath('//div[@class="typography table-responsive"]/table').xpath('//td[9]/text()').extract()
            body=response.xpath('//div[@class="typography table-responsive"]/table').xpath('//td[11]/text()').extract()
    
            l.add_value("poradi_tymu", poradi_tymu)  
            l.add_value("tym", tym)
            l.add_value("pocet_utkani", pocet_utkani)
            l.add_value("pocet_vitezstvi", pocet_vitezstvi)
            l.add_value("pocet_remiz", pocet_remiz)
            l.add_value("pocet_proher", pocet_proher)        
            l.add_value("skore", skore) 
            l.add_value("body", body)
            l.add_value("kolo", kolo) 
            #vystup
            return l.load_item()

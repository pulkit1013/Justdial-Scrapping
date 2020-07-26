import scrapy
from ..items import Justdial2Item
import re


class InformationSpider(scrapy.Spider):
    name = 'information'
    
    start_urls = [
        'https://www.justdial.com/Delhi/House-On-Rent/nct-10192844'
    ]

    def parse(self, response):
        items= Justdial2Item()

        name=response.css(".lng_cont_name::text").extract()
        rating=response.css(".green-box::text").extract()
        phone=response.css(".contact-info").extract()  
        address=response.css(".cont_sw_addr::text").extract()

        
        for i,p in enumerate(phone):
            p=p.replace('\"></span><span class=\"mobilesv ','_')
            p=p[217:-31]
            p=p.split("_")
            
            for index,number in enumerate(p):
                if number =="icon-yz":
                    p[index]='1'
                elif number=='icon-wx':
                    p[index]='2'
                elif number=='icon-vu':
                    p[index]='3'
                elif number=='icon-ts':
                    p[index]='4'
                elif number=='icon-rq':
                    p[index]='5'
                elif number=='icon-po':
                    p[index]='6'
                elif number=='icon-nm':
                    p[index]='7'
                elif number=='icon-lk':
                    p[index]='8'
                elif number=='icon-ji':
                    p[index]='9'
                elif number=='icon-acb':
                    p[index]='0'
                elif number=='icon-ba':
                    p[index]='-'
                    
                phone[i]=p
                
            separator = ''
            phone[i]=separator.join(p)

        for index,addr in enumerate(address):
            address[index]=addr[13:-9]
        
        items['name']=name
        items['rating']=rating
        items['phone']=phone
        items['address']=address

        for i in range(0,len(items)):
            yield {
                'name':items['name'][i],
                'rating': items['rating'][i],
                'phone': items['phone'][i],
                'address': items['address'][i]
            }

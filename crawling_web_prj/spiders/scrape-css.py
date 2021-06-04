from os import execl
import scrapy
import pandas as pd
import re

class ToScrapeCSSSpider(scrapy.Spider):
    

    name = "scrape-css"
    start_urls = [
        'https://news.ycombinator.com/'
    ]

    def parse(self, response):
       #array initialization for excel creation
        order_number =[]
        title = []
        comments = []
        points = []
        #Tittle an order data extract
        for register in response.css("tr.athing"):
            order_number.append(register.css("td.title > span.rank::text").extract_first())
            title.append(register.css("td.title > a.storylink::text").extract_first()) 
            yield {
                'order_number': register.css("td.title > span.rank::text").extract_first(),
                'title': register.css("td.title > a.storylink::text").extract_first(),
            }
        #Points and comments number extraction
        for information in response.css("td.subtext"):
            comments.append(information.xpath('..//td[2]/a[3]/text()').extract_first())
            points.append(information.css("span.score::text").extract_first())
            yield {
                'comments': information.xpath('..//td[2]/a[3]/text()').extract_first(),
                'points': information.css("span.score::text").extract_first()
            }
        final_comments = []
        final_points = []
        for com in comments:
            if com and not com == "discuss":
                for C_ in com.split():
                    if C_.isdigit():
                        final_comments.append(int(C_))
            else:
                final_comments.append(0)
        for Po_ in points:
            if Po_:
                for P_ in Po_.split():
                    if P_.isdigit():
                        final_points.append(int(P_))
            else:
                final_points.append(0)   
        ultimate_array = []
        for i in range(len(order_number)):
            dic = {"Order Number": order_number[i-1], "Title": title[i-1], "Comments": final_comments[i-1], "Points": final_points[i-1]}
            ultimate_array.append(dic)
        more_5_array = []
        less_5_array = []
        for X in ultimate_array:
            if len(X.get("Title").split()) > 5:
                more_5_array.append(X)
            else:
                less_5_array.append(X)
        sorted_more_com = sorted(more_5_array, key=lambda k: k["Comments"])
        sorted_more_fp = sorted(less_5_array, key=lambda k: k["Points"])
        #Excel file creation 
        df = pd.DataFrame(ultimate_array)
        df2 = pd.DataFrame(sorted_more_com)
        df3 = pd.DataFrame(sorted_more_fp)
        df.to_excel("../crawling_web_prj/acumulative.xlsx", sheet_name='acumulative')
        df2.to_excel("../crawling_web_prj/filter_comments.xlsx", sheet_name='filter_comments')
        df3.to_excel("../crawling_web_prj/filter_points.xlsx", sheet_name='filter_points')
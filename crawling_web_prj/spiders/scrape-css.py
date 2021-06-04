from os import execl
import scrapy
import pandas as pd

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
        for register in (response.css("tr.athing") ):
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
        
   
        #Excel file creation for original data exporting
        final_array = [order_number, title, comments, points]
        df = pd.DataFrame(final_array).T
        df.rename(columns= {'0':'order_number', '1':'title', '2':'comments', '3':'points'}, inplace=False)
        df.to_excel(excel_writer="../crawling_web_prj/data_extracted.xlsx")
        
        print('imprimiendo')
        for i in range(len(order_number)):
            print(order_number[1])




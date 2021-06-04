# Hacker News crawling
This is a Scrapy project example to scrape information of Hacker News web page.

## Extracted Data

This project extracts information of the news just like: order number, title, comments number and ponts.
The data extracted is exported to a xlsx file to review and also a .json or .jl file

The data is going to lool like
  [
    {
      'order_number': '',
      'title': ''
    }
    {
      'comments' : ''
      'points' : ''
     }
  ]
  
 ##Spiders 
 
 The spider used for this crawling is scrape-css.py here to extract the information are used css selectors mostly, and an xpath for comments.
 
 
##How to run spiders

You can run a spider using the `scrapy crawl` command, such as:

    $ scrapy crawl scrape-css

If you want to save the scraped data to a file as it was mentioned before to a JSON or JL, you can pass the `-O` option:
    
    $ scrapy crawl scrape-css -o data_extracted.json
    $ scrapy crawl scrape-css -o data_extracted.jl

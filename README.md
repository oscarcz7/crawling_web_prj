# Hacker News crawling
This is a Scrapy project example to scrape information of Hacker News web page.

## Extracted Data

This project extracts information of the news just like: order number, title, comments number and ponts.
The data extracted is exported to three different xlsx files where are all data retrieved, and the different filters to review, also a .json or .jl file

## Requirements 

      'Pandas': 'pip install pandas',
      'Scrapy': 'pip install scrapy',
      
  
## Spider
 
The spider used for this crawling is scrape-css.py here to extract the information are used css selectors mostly, and an xpath for comments.
 

## How to run spiders

You can run a spider using the `scrapy crawl` command, such as:

    $ scrapy crawl scrape-css

This will generate the excel files at the root folders

If you want to save the scraped data to a file as it was mentioned before to a JSON or JL file at the root folder, you can pass the `-O` option:
    
    $ scrapy crawl scrape-css -o data_extracted.json
    $ scrapy crawl scrape-css -o data_extracted.jl

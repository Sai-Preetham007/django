import scrapy

class Quotes_Spider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):               # the function name should be 'start_requests'.
        urls = [
            "https://quotes.toscrape.com/page/1/",        # we need to specify the web url's manually.
            "https://quotes.toscrape.com/page/2/"         # we will see the automation process in fully_automated_quotes.py.
        ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    
    def parse(self, response):
        page_id = response.url.split("/")[-2]
        file_name = f"page{page_id}.html"

        with open(file_name, "wb") as file:
            file.write(response.body)
        
        self.log(f"log file : {file_name}")
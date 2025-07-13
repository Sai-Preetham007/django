import os
import scrapy

class Quotes(scrapy.Spider):
    name = "automated_quotes"

    def start_requests(self):
        base_url = "https://quotes.toscrape.com/page/1/"

        yield scrapy.Request(url=base_url, callback=self.parse)

    
    def parse(self, response):

        os.makedirs("quotes_html", exist_ok=True)         # making a new folder

        page_id = response.url.split("/")[-2]
        file_name = f"quotes_html/page_{page_id}_quotes.html"


        with open(file_name, "wb") as file:
            file.write(response.body)
    

        for quote in response.css("div.quote"):
            text = quote.css("span.text::text").get()
            author = quote.css("span small.author::text").get()
            tags = quote.css("div.tags a.tag::text").getall()
        
            yield {"Text" : text, "Author" : author, "Tags" : tags}


        next_url = response.css("nav ul.pager li.next a::attr(href)").get()
        if next_url is not None:
            next_url = response.urljoin(next_url)
            yield scrapy.Request(url=next_url, callback=self.parse)


# Run the below command in the terminal.
# scrapy crawl automated_quotes -o all_quotes.json
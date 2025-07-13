import scrapy

class Quotes_Spider(scrapy.Spider):
    name = "quotes-1"

    def start_requests(self):                # The function name should 'start_requests'.
        urls = [
            "https://quotes.toscrape.com/page/1/",
            "https://quotes.toscrape.com/page/2"
        ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

        
    def parse(self, response):

        for quote in response.css("div.quote"):
            text = quote.css("span.text::text").get()[1:-1]
            author = quote.css("span small.author::text").get()
            tags = quote.css("div.tags a.tag::text").getall()

            yield {
                "Text" : text,
                "Author" : author,
                "Tags" : tags
            }                   # saving all the yielded output in a json file.

# Go to terminal type ---> scrapy crawl {class_name} -o {output file name}
#                     ---> scrapy crawl quote-1 -o quotes.json
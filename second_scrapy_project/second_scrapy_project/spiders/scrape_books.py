import scrapy

class Books(scrapy.Spider):
    name = "books"

    def start_requests(self):
        base_url = "https://books.toscrape.com/"

        yield scrapy.Request(url=base_url, callback=self.parse)


    def parse(self, response):
        for card in response.css("article.product_pod"):
            title = card.css("h3 a::attr(title)").get()
            image = card.css("img.thumbnail::attr(src)").get()
            rating = card.css("p::attr(class)")[0].get().split()[-1]
            price = card.css("p.price_color::text").get()

            yield {
                "Title" : title,
                "Image" : image,
                "Rating" : rating,
                "Price" : price
            }


        next_page = response.css("ul.pager li.next a::attr(href)").get()
        if next_page:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(url=next_page, callback=self.parse)

# open terminal and execute the below folloing codes.

# scrapy crawl books -o books.json
# scrapy crawl books -o bokks.csv
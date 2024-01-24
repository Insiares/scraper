import scrapy
from brief10.items import QuoteItem


class QuoteSpider(scrapy.Spider):
    name = "quotes"
    start_urls = ["https://quotes.toscrape.com/"]

    def parse(self, response):
        for quote in response.css("div.quote"):
            item = QuoteItem()
            item["content"] = quote.css("span.text::text").get()
            item["author"] = quote.css("small.author::text").get()
            yield item

        # follow pagination link
        next_page = response.css("li.next a::attr(href)").get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)

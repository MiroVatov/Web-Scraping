import scrapy
from quotetutorial.items import QuotetutorialItem


class QuoteSpider(scrapy.Spider):

    name = 'quotes'
    page_number = 2
    start_urls = [
        'https://quotes.toscrape.com/page/1/'
    ]

    def parse(self, response, **kwargs):
        items = QuotetutorialItem()

        all_div_quotes = response.css('div.quote')

        for quotes in all_div_quotes:
            title = quotes.css('span.text::text').extract()
            author = quotes.css('.author::text').extract()
            tag = quotes.css('.tag::text').extract()

            items['title'] = title
            items['author'] = author
            items['tag'] = tag

            yield items

        # Method to scrape multiple pages, with recursive callback function (self.parse) below.
        # After executing the for loop above, the IF condition checks if there are more pages to scrape with (next_page) response.
        # It is performed until next page is None.

        """ Below is the First Version to call the next page with the response.css('li.next a::attr(href)').get() """

        # next_page = response.css('li.next a::attr(href)').get()
        #
        # if next_page is not None:
        #     yield response.follow(next_page, callback=self.parse)

        """ Below is the Second Version to call the next page with class variable page_number, which increments on every iteration until it gets to the final page number """

        next_page = f'https://quotes.toscrape.com/page/{QuoteSpider.page_number}/'
        if QuoteSpider.page_number < 11:
            QuoteSpider.page_number += 1
            yield response.follow(next_page, callback=self.parse)

import scrapy
from scrapy.http import FormRequest
from scrapy.utils.response import open_in_browser
from quotetutorial.items import QuotetutorialItem


class QuoteSpider(scrapy.Spider):

    """ Below is the Form Request Filler, in order to be logged into the site when we scrape the data from the site """

    name = 'quotes'
    start_urls = [
        'https://quotes.toscrape.com/login'
    ]

    def parse(self, response, **kwargs):
        token = response.css('form input::attr(value)').extract_first()

        return FormRequest.from_response(response, formdata={""" Below we fill in the login data needed to login """
            'csrf_token': token,
            'username': 'totalmikro1',  # input random username and password
            'password': '123'
        }, callback=self.start_scraping)  # The last parameter in the FormRequest is callback function, which is the action, which has to be performed when we are logged into the website

    def start_scraping(self, response):
        open_in_browser(response)
        """ We copy the parse function/method from the backup file """

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
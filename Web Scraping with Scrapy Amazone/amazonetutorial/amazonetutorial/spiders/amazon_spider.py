import scrapy
from amazontutorial.items import AmazontutorialItem


class AmazonSpiderSpider(scrapy.Spider):
    name = 'amazon'
    page_number = 2
    start_urls = [
        'https://www.ebay.com/b/Xiaomi-Cell-Phones-Smartphones/9355/bn_315817'
        # 'https://www.amazon.com/s?k=Last+30+Days&i=stripbooks-intl-ship&ref=nb_sb_noss_2'
        # 'https://www.amazon.com/s?bbn=283155&rh=n%3A283155%2Cp_n_publication_date%3A1250226011&dc&qid=1625658227&rnid=1250225011&ref=lp_1000_nr_p_n_publication_date_0'
    ]

    def parse(self, response, **kwargs):

        """ Version for E-Bay data scraping """
        items = AmazontutorialItem()

        product_name = response.css('.s-item__title::text').extract()
        product_price = response.css('.s-item__price').css('::text').extract()
        product_imagelink = response.css('.s-item__image-img::attr(src)').extract()

        items['product_name'] = product_name
        items['product_price'] = product_price
        items['product_imagelink'] = product_imagelink

        yield items

        next_page = 'https://www.ebay.com/b/Xiaomi-Cell-Phones-Smartphones/9355/bn_315817?_pgn=' + f'{AmazonSpiderSpider.page_number}'

        if AmazonSpiderSpider.page_number <= 100:
            AmazonSpiderSpider.page_number += 1
            yield response.follow(next_page, callback=self.parse)

    """ Below Version for Amazon Web scraping """

    # def parse(self, response, **kwargs):
    #     items = AmazontutorialItem()
    #
    #     """ Version 1 - Amazon scraping """
    #
    #     product_name = response.css('.a-color-base.a-text-normal::text').extract()
    #     product_author = response.css('.a-color-secondary .a-row .a-size-base+ .a-size-base').css('::text').extract()
    #     # product_price = response.css('.a-spacing-top-small .a-price-fraction , .a-spacing-top-small .a-price-whole').css('::text').extract()
    #     product_imagelink = response.css('.s-image::attr(src)').extract()
    #
    #     """ Version 2 - Amazon scraping """
    #
    #     # product_name = response.css('.a-color-base.a-text-normal::text').extract()
    #     # product_author = response.css('.a-color-secondary .a-row span.a-size-base+ .a-size-base , .a-color-secondary .a-size-base.a-link-normal').css('::text').extract()
    #     # product_price = response.css('.a-spacing-top-small .a-price-fraction , .a-spacing-top-small .a-price-whole').css('::text').extract()
    #     # product_imagelink = response.css('.s-image::attr(src)').extract()
    #
    #     items['product_name'] = product_name
    #     items['product_author'] = product_author
    #     # items['product_price'] = product_price
    #     items['product_imagelink'] = product_imagelink
    #
    #     yield items
    #
    #     """ Version 1 - Amazon scraping """
    #     # next_page = 'https://www.amazon.com/s?i=stripbooks&bbn=283155&rh=n%3A283155%2Cp_n_publication_date%3A1250226011&dc&page=' + f'{AmazonSpiderSpider.page_number}' +'&qid=1625658237&rnid=1250225011&ref=sr_pg_2'
    #
    #
    #     """ Version 2 - Amazon scraping """
    #     next_page = 'https://www.amazon.com/s?k=Last+30+Days&i=stripbooks-intl-ship&page=' + f'{AmazonSpiderSpider.page_number}' +'&qid=1625670018&ref=sr_pg_2'
    #
    #     if AmazonSpiderSpider.page_number <= 100:
    #         AmazonSpiderSpider.page_number += 1
    #         yield response.follow(next_page, callback=self.parse)

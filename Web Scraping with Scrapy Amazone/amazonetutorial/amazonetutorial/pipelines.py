# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import pymongo


class AmazontutorialPipeline:
    def __init__(self):
        self.conn = pymongo.MongoClient(  # creating the connection with the MongoDB Server, in order to be visible in the MonogDB Compass App
            'localhost',
            27017,
        )
        db = self.conn['amazon_scraping']  # Creating a database
        self.collection = db['amazon_tb']  # Creating a table

    def process_item(self, item, spider):
        self.collection.insert(dict(item))
        return item

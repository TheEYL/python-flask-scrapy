# -*- coding: utf-8 -*-
import psycopg2
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class MoviescraperPipeline(object):

    def open_spider(self, spider):
        hostname = 'localhost'
        username = 'learningflask'# the username when you create the database
        password = 'leo' #change to your password

        database = 'learningflask'
        self.connection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)
        self.cur = self.connection.cursor()


    def close_spider(self, spider):
        self.cur.close()
        self.connection.close()

    def process_item(self, item, spider):
        try:
            self.cur.execute("insert into movies ( title, url, image) values(%s,%s, %s )",(item['title'],item['url'], item['img']))
            self.connection.commit()
            # return item
        except Exception as e:
            self.connection.rollback()
            print(repr(e))
        # return item




        # saving reviews
        # reviews = item["reviews"]
        #
        # for review in reviews:
        #     review_date = review["review_date"]
        #     print("DATTEEEEE:")
        #     print(review_date)
        #     # review_date = self.convert_date(review_date)
        #     sql = "insert into reviews (review_id, book_id_id, subject, author, rating, review_text) " \
        #           "VALUES ('%s', '%s', '%s', '%s', '%s', '%s'   )" % \
        #           (review["review_id"], item["book_id"], review["subject"], review["author"], review["rating"],
        #            review["review_body"])
        #     try:
        #         self.cur.execute(sql)
        #         self.connection.commit()
        #     except Exception as e:
        #         self.connection.rollback()
        #         print(repr(e))
        #         print(item["book_id"])

   # @staticmethod
   # def convert_date(date_string):
   #      # date_object = datetime.strptime(date_string, "%m/%d/%Y")
   #      # return date_object
   #      return date_string

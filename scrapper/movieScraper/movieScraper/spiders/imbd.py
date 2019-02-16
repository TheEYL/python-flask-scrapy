# -*- coding: utf-8 -*-
import scrapy
from scrapy import signals
from movieScraper.items import MoviescraperItem
from movieScraper.items import ImbdMovieList

class ImbdSpider(scrapy.Spider):
    name = 'imdb_scrap'
    allowed_domains = ['www.imdb.com']
    start_urls = ['http://www.imdb.com/chart/top/']

    moviedict = {}
    images = []
    def parse(self, response):
        # table = response.xpath('//td[@class="titleColumn"]/a/text()')
        # print(table)
        self.getList(response)

        self.getListAndLinks(response)
        # pass
        for k,next_url in ImbdSpider.moviedict.items():
            yield scrapy.Request(next_url,callback=self.getPosters)
    #
    # def yieldMovies():
    #     # import time
    #     # time.sleep(120)
    #     movie = MoviescraperItem()
    #     i = 0
    #     for k,v in  ImbdSpider.moviedict.items():
    #         print("are you alive?")
    #         movie["title"] = k;
    #         movie["url"] = v;
    #         while (i<250):
    #             movie["img"] = ImbdSpider.images[i]
    #             i = i + 1
    #
    #         print(movie)
    #         # yield movie
    #
    def getPosters(self, response):
        href = response.xpath('//div[@class="poster"]/a/@href').extract()[0] #img
        imgurl = response.urljoin(href)

        movie = MoviescraperItem()
        movie["title"] = response.xpath('//div[@class="title_wrapper"]/h1/text()').extract_first()
        movie["url"] = response.url
        movie["img"] = imgurl
        yield movie
        # print(movie)
        # response.xpath('//div[@class="poster"]/a[@href]/img/@src') #posters
        # pass
        # ImbdSpider.images.append(imgurl)


    @staticmethod
    def getListAndLinks(response):

        table = response.xpath('//td[@class="titleColumn"]') #movies and links
        # movie = MoviescraperItem()

        for i in table:
            ImbdSpider.moviedict[i.xpath('a/text()').extract()[0]] = response.urljoin(i.xpath('a/@href').extract()[0])
           # yield scrapy.Request(movie["url"], callback=self.getPosters)
           # yield movie
        # print(moviedict)
           # yield movie


    @staticmethod
    def getList(response):
        """ Get movie list"""
        movie_list =  ImbdMovieList()
        table = response.xpath('//td[@class="titleColumn"]/a/text()')
        movie_list = table.extract()
        movies  = []
        for item in movie_list:
             if (item !=' ' and item !='\n'):
                     movies.append(item)
        movie_list=movies
        # yield movie_list

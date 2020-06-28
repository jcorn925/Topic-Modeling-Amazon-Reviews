# -*- coding: utf-8 -*-
import scrapy
from ..items import ReviewsItem

class AmazonSpiderSpider(scrapy.Spider):
    name = 'amazon'
    start_urls = [
        'https://www.amazon.com/RiptGear-Compression-Knee-Sleeve-Stabilizer/product-reviews/B07RF9KQH6/ref=cm_cr_arp_d_viewpnt_rgt?ie=UTF8&reviewerType=all_reviews&filterByStar=critical&pageNumber=1'
    ]

    def parse(self, response):
        items = ReviewsItem()

        review = response.css('.review-text-content span::text').extract()
        #stars = response.css('.review-rating::text').extract()
        #title = response.css('.a-text-bold span::text').extract()

        items['review'] = review
        #items['stars'] = stars
        #items['title'] = title

        yield items

        next_page = response.css('li.a-last a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback= self.parse)

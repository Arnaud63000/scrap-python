import re
import scrapy
import unicodedata
from scrapy_splash import SplashRequest
from scrapy.shell import inspect_response


class Scrap(scrapy.Spider):
    name = "Scrap"
    start_urls = ["https://www.youtube.com/"]

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url, self.parse,
                                endpoint='render.html',
                                args={'wait': 0.5},
                                )

    def parse(self, response):
        print("ici")
        for video in response.css('.yt-shelf-grid-item'):
            print("Une video")

            inspect_response(response, self)
            
            yield{
                'title': video.css('.spf-link::attr(title)').extract_first().encode('utf-8'),
                'duration': video.css('.accessible-description::text').extract_first().encode('utf-8'),
                'link': video.css('.spf-link::attr(href)').extract_first().encode('utf-8'),
            }

        # page = response.url.split("/")[-2]
        # filename = 'youtube-%s.html' % page
        # titles = response.css('.yt-lockup-title')

        # for i in titles:
        #titles[0].css('::text').extract_first()
        
        # inspect_response(response, self)

        # yield {
        # 'title': ,
        # 'length': ,
        # 'link': ,
        # }

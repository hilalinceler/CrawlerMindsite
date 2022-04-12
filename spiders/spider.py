from asyncio.windows_events import NULL
import scrapy
from scrapy import Request
from scrapy.spiders import SitemapSpider
from scrapy.spidermiddlewares.httperror import HttpError
from twisted.internet.error import DNSLookupError
from twisted.internet.error import TimeoutError, TCPTimedOutError, ConnectionRefusedError

from CrawlerMindsite.items import CrawlermindsiteItem

class Spider(scrapy.Spider):
    name = 'spider'
    allowed_domains = ['www.trendyol.com']
    start_urls = ['http://www.trendyol.com/']

    def parse(self, response):
        try:
            for value in response.css('li'):
                if  value.css("a.category-header::text").get() != None: #örnek olması için class ı category-header olan textleri aldım, değiştirlebilir ihtiyaca göre. 
                    yield {
                        'text': value.css("a.category-header::text").get(),
                    }
        except ValueError:
            self.logger.error(repr(ValueError))

            if ValueError.check(HttpError):
                response = ValueError.value.response
                self.logger.error('HttpError on %s', response.url)

            elif ValueError.check(TimeoutError, TCPTimedOutError):
                request = ValueError.request
                self.logger.error('TimeoutError on %s', request.url)

            elif ValueError.check(ConnectionRefusedError):
                request = ValueError.request
                self.logger.error('ConnectionRefusedError on %s', request.url)

    
        
            

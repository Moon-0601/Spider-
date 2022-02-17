# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
import random
import base64


# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter


class SpidersSpiderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, or item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request or item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class SpidersDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class  useragentMiddleware(object):
    version_id=random.randint(50,100)
    os_type= ['Windows NT 10.0','Windows NT 6.1','linux 10.0']
    USER_AGENT="Mozilla/5.0 ("+random.choice(os_type)+"; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758."+str(version_id)+" Safari/537.36"
    def process_requests(self,request,spider):
        request.header['User-Agent']=self.USER_AGENT
        pass


#代理ip的中间件
class proxyMiddleware(object):
    #普通代理
    PROXIES={'1.2.3.4:8080','2.3.4.4:9090'}
    def process_request(self,request,spider):

        proxy=random.choice(self.PROXIES)
        request.meta['proxy']=proxy
        """
        #有单独用户名和密码的私密代理
        proxy='1.3.4.5:9099'
        user_pass="admin:admin8888"
        request.meta['proxy']=proxy
        #假如需要使用base64加密
        bs64_user_pass=base64.b64encode(user_pass.encode('utf-8'))
        request.headers['Proxy-Authorization']="Basic"+bs64_user_pass.decode("utf-8")
        """
        pass

    def process_response(self,request,response,spider):
        if response.status!=200:
            print('请求出错')




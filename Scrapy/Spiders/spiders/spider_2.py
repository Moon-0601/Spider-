import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from Spiders.items import SpidersItem


class Spider2Spider(CrawlSpider):
    name = 'spider_2'
    allowed_domains = ['4399dmw.com']
    start_urls = ['http://www.4399dmw.com/search/dh-1-0-0-0-0-1-0/']

    #决定爬虫的走向
    rules = (
        Rule(LinkExtractor(allow=r".+dh-1-0-0-0-0-([0-9]|[1-9][0-9])-0\/"),follow=True),
        Rule(LinkExtractor(allow=r".+\/dh\/.+\/"), callback='parse_follow', follow=False),

    )

    def parse_item(self, response):
        item = {}
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        datas_pic = response.xpath("/html/body/div[2]/div[2]/div/div[2]/div[2]/a/img")
        for item in datas_pic:
            # 使用items来存储
            # topipeline1={'Title':item.get()}
            pic = item.xpath("@data-src").extract()[0]
            title = item.xpath("@alt").extract()[0]
            topipeline1 = SpidersItem(title=title, pic=pic)
            yield topipeline1
        return item


    def parse_follow(self,response):
        title=response.xpath("//div[@class='works__main']/h1/text()").extract()[0]
        pic="http:"+response.xpath("//div[@class='works__left']/img/@data-src").extract()[0]
        jianjie=response.xpath("//div[@class='main']/div/p/text()").extract()[0]
        topipeline2 = SpidersItem(title=title,pic=pic,jianjie=jianjie)
        yield topipeline2

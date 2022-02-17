import scrapy
from Spiders.items import SpidersItem


class Spider1Spider(scrapy.Spider):
    #爬虫根据这个名字运行
    name = 'spider_1'
    #允许的域名
    allowed_domains = ['4399dmw.com']
    #从什么域名开始
    start_urls = ['http://www.4399dmw.com/search/dh-1-0-0-0-0-1-0/']

    def parse(self, response):
        #文字地址--/html/body/div[2]/div[2]/div/div[2]/div[2]/a/div/p
        #图片地址--/html/body/div[2]/div[2]/div/div[2]/div[2]/a/img
        #datas=response.xpath('/html/body/div[2]/div[2]/div/div[2]/div[2]/a/div/p/text()')
        datas_pic=response.xpath("/html/body/div[2]/div[2]/div/div[2]/div[2]/a/img")
        for item in datas_pic:
            # 使用items来存储
            #topipeline1={'Title':item.get()}
            pic=item.xpath("@data-src").extract()[0]
            title=item.xpath("@alt").extract()[0]
            topipeline1=SpidersItem(title=title,pic=pic)
            yield topipeline1



        #找到下一页的链接
        next_url=response.xpath("//a[contains(text(),'下一页')]/@href").get()
        if not next_url:
            #如果没有下一页就停止
            return
        else:
            #让他返回继续执行这个方法
            yield scrapy.Request("http://www.4399dmw.com/"+next_url,callback=self.parse)

        pass

    # ####如果需要发送post数据
    # def start_requests(self):
    #     url="http://www.xx.com"
    #     data={"username":"admin","passwd":"admin"}
    #     #请求地址和数据，进行回调
    #     request=scrapy.FormRequest(url,formdata=data,callback=self.parse_login)
    #     yield request
    #     pass
    #
    # def parse_login(self,response):
    #     with open("xx.html","w",encoding="utf-8")as fp:
    #         fp.write(response.text)
    #     pass
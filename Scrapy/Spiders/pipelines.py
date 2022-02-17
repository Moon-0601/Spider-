# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import requests
from itemadapter import ItemAdapter
import json
import os
from Spiders import settings
from urllib import request
from scrapy.pipelines.images import ImagesPipeline
from scrapy import Request
#from scrapy.exporters import JsonItemExporter,JsonLinesItemExporter #不适合数据量大的情况
#JsonItemExporter--一行导出,JsonLinesItemExporter--换行导出

class SpidersPipeline:
    """定义数据处理的方式"""

    #打开爬虫的时候执行
    def open_spider(self,spider):
    #     #打开并准备存储
    #     self.fp=open("F:\Py-Pro\Spider\Spiders\Spiders\spiders\Spr_1存储\ s1.json","w",encoding="utf-8")
    # #判断路径是否存在
        #self.path=os.path.join(os.path.dirname(os.path.dirname(__file__)),'images')
        self.path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'videos')
        if not os.path.exists(self.path):
            os.mkdir(self.path)



        # # 打开并准备存储，使用二进制存储
        # self.fp=open("F:\Py-Pro\Spider\Spiders\Spiders\spiders\Spr_1存储\ s1.json","wb")
        # self.exporter=JsonItemExporter(self.fp,ensure_ascii=False,encoding="utf-8")
        # self.exporter.start_exporting()


        pass

    #使用yield时运行(协程)
    def process_item(self, item, spider):
    # #item_json=json.dumps(item,ensure_ascii=False)
    # item_json=json.dumps(dict(item),ensure_ascii=False)
    # self.fp.write(item_json+'\n')
    # #获得item的细节
    # title=item['title']
    # pic=item['pic']
    # path1=os.path.join(self.path,'pic1')
    # if not os.path.exists(path1):
    #     os.mkdir(path1)
    # ## 下载图片并且加上ipg后缀名
    # request.urlretrieve(pic, os.path.join(path1,title+'.jpg' ))
        """"==============================================================="""
        """video下载"""
        file_name=item['file_name']
        min_title=item['title']
        res = item['saved_video']
        path2 = os.path.join(self.path,"%s"%file_name )
        save_path=os.path.join(path2,min_title+".mp4")

        if not os.path.exists(path2):
            os.mkdir(path2)
        with open(save_path,"wb")as f:
            f.write(res)





        # self.exporter.export_item(item)
        return item

    #结束爬虫的时候执行
    def close_spider(self,spider):
        # self.exporter.finish_exporting()

        # #结束关闭文件
        # self.fp.close()
        pass

####重写图片下载类
class newImagePipeline(ImagesPipeline):
    #请求之前调用（super重写方法）
    def get_media_requests(self, item, info):
        # request_objs=super(newImagePipeline,self).get_media_requests(item,info)
        # for request_obj in  request_objs:
        #     request_obj.item=item
        # return request_objs
        for image_url in item['pic'][0]:
            yield Request(image_url,meta={'name':item['title'][0]})

    #请求之后调用
    def file_path(self, request, response=None, info=None, *, item=None):
        #重写path方法
        path=super(newImagePipeline,self).file_path(request,response,info)
        #获得图片类型以新建文件夹
        category=request.item.get('category')
        #获得settings里的图片路径
        image_store=settings.IMAGE_STORE
        category_path=os.path.join(image_store,category)
        if not os.path.exists(category_path):
            os.mkdir(category_path)
        #修改原有图片的名字
        image_name=path.replace()
        #真正图片路径
        image_path=os.path.join(category_path,image_name)
        return image_path





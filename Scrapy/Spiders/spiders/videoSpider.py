import requests
import scrapy
import re
import os
from Spiders.items import SpidersItem
from scrapy import Request
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


class VideospiderSpider(CrawlSpider):
    name = 'videoSpider'
    allowed_domains = ['ddrk.me']
    start_urls = ['https://ddrk.me/category/anime/']

    rules = (
        Rule(LinkExtractor(allow=r'.+\/anime\/page\/1\/'), callback='parse_item', follow=True),

    )

    def Click_start(self,url):
        options = webdriver.ChromeOptions()
        tar_dri = Service(executable_path=r"F:\Py-Pro\Spider\chromedriver.exe")
        location = r"F:\Py-Pro\Spider\chrome-win\chrome.exe"
        options.binary_location = location
        #### 增加user-agent
        options.add_argument(
            'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36')

        options.add_experimental_option('excludeSwitches', ['enable-automation'])
        options.add_argument("headless")
        driver = webdriver.Chrome(service=tar_dri, options=options)

        driver.get(url)
        driver.find_element(By.XPATH, "//button[@class='vjs-big-play-button']").click()
        time.sleep(2)
        tar_url=driver.find_element(By.XPATH,"//div[@class='wp-playlist wp-video-playlist wp-playlist-light wpse-playlist']/div[@class='video-js vjs-default-skin vjs-big-play-centered vjs-fluid vjs-playback-rate vjsp-dimensions vjs-controls-enabled vjs-workinghover vjs-v7 vjs-theater-mode vjs-has-started vjs-paused vjs-user-inactive']/video/@src")[0]

        print(tar_url)
        return tar_url
    def parse_item(self, response):
        item = SpidersItem()
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        sigle_dm_URL=response.xpath("//div[@class='post-box-list']/article/@data-href").extract()

        for url in sigle_dm_URL:
            item['url']=url
            yield scrapy.Request(url,meta=item,callback=self.parse_detail)
        return item

    def parse_detail(self,response):
        #item=response.meta
        #Download_url=response.xpath("//div[@class='wp-playlist wp-video-playlist wp-playlist-light wpse-playlist']/div[@class='video-js vjs-default-skin vjs-big-play-centered vjs-fluid vjs-playback-rate vjsp-dimensions vjs-controls-enabled vjs-workinghover vjs-v7 vjs-theater-mode vjs-has-started vjs-paused vjs-user-inactive']/video/@src").extract()[0]
        item=response.meta
        befor_url=item['url']
        Download_url=self.Click_start(befor_url)
        print(Download_url)
        item['file_name']=response.xpath("//div[@class='post-content']/h1/text()").extract()[0]

        dm_detil_title=response.xpath("//div[@class='wp-playlist-item wp-playlist-playing']/a/text()").extract()[0]

        for title in dm_detil_title:
            before = re.compile('.\.(.+)')
            item['title']= before.findall(title)[0].strip()
        #yield scrapy.Request(url=Download_url,meta=item,callback=self.Download_dm)

        pass

    def Download_dm(self,response):
        item=response.meta
        file_name = item['file_name']
        min_title = item['title']
        path2 = os.path.join("F:/Py-Pro/Spider/Spiders/videos",file_name)
        save_path = os.path.join(path2, min_title + ".mp4")

        if not os.path.exists(path2):
            os.mkdir(path2)
        with open(save_path, "wb") as f:
            f.write(response.body)

        pass
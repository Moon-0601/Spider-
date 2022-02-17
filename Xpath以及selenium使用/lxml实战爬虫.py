import requests
from lxml import etree

####    页面内爬虫
def spider(url):
    ####获取网页源码
    url = url
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.81 Safari/537.36"
    }
    resp = requests.get(url=url, headers=headers)
    html_doc = resp.content.decode("utf-8")

    ####lxml处理
    # 使用etree转化html_doc，转化为了一个html的对象，此时element对象可以使用xpath语法
    html = etree.HTML(html_doc)

    src=html.xpath("//div[@class='lst']/a[@class='u-card']/img/@data-src")
    columns_list=html.xpath("//div[@class='lst']/a[@class='u-card']")
    num=len(columns_list)+1
    for i in range(1,num):
        mz=html.xpath("//div[@class='lst']/a[@class='u-card'][{}]/div/p/text()".format(i))
        src = html.xpath("//div[@class='lst']/a[@class='u-card'][{}]/img/@data-src".format(i))
        real_src="http:"+src[0]
        prt=mz[0]+"------"+real_src
        print(prt)

    pass

####    发现下一页的爬虫
def find_next_page(url):
    url=url
    headers = {
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1",
        "Referer": "http://www.baidu.com"
    }
    resp = requests.get(url=url, headers=headers)
    html_doc = resp.content.decode("utf-8")
    html = etree.HTML(html_doc)

    ####高效爬取下一页链接
    next_page = html.xpath("// a[contains(text(), '下一页')] / @ href")
    real_next_page = "http://www.4399dmw.com" + next_page[0]
    return real_next_page

def main():
    url = "http://www.4399dmw.com/search/dh-1-0-0-0-0-1-0/"
    p=1
    print("---!!!各单位请注意！！！---\n"+"---!!!Spider开始爬行!!!---\n"+"==========================================================\n")
    while True:
        try:
            print("Page%d:"%p+url+"\n")
            spider(url)
            print("======================================")
            url=find_next_page(url)
            p=p+1
        except:

            break
    print("~~~宝~好啦好啦~~~")

    pass

if __name__ == '__main__':
    main()





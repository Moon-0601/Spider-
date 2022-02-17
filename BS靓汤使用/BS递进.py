import requests
from bs4 import BeautifulSoup

# def spider(page):
#     url = "http://www.4399dmw.com/search/dh-1-0-0-0-0-{}-0/".format(page)
#     headers = {
#         "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1",
#         "Referer": "http://www.baidu.com"
#     }
#     resp = requests.get(url=url, headers=headers)
# # 保存页面源代码
#     html_doc = resp.content.decode("utf-8")
#
# # 使用BS处理网页源代码
#     soup = BeautifulSoup(html_doc,'html.parser')
#
#     list = soup.find('div',class_='lst').find_all('a',class_='u-card')
#     for item in list:
#         #取出所有list中每一项的细节
#         mz=item.find('p',class_='u-tt').get_text()
#         #取出图片地址
#         src="http:"+item.find('img').get('data-src')
#         text=mz+"------"+src
#         with open("F:/Py-Pro/Spider/爬虫基础/test/4399动漫--Page"+str(page)+".txt", "a",encoding="utf-8") as f: #'a'表示文本追加
#             f.write(text+"\n")
#     pass
#
#
# def main():
#     for i in range(1,15):
#         spider(i)
#         print("Page"+str(i)+"was saved successfully!\n")
#     print("------------\n"+"芜湖！成功啦！")

####递进爬取火影忍者页面信息
def spider(page):
    url = "http://www.4399dmw.com/search/dh-1-0-0-0-0-{}-0/".format(page)
    headers = {
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1",
        "Referer": "http://www.baidu.com"
    }
    resp = requests.get(url=url, headers=headers)
# 保存页面源代码
    html_doc = resp.content.decode("utf-8")

# 使用BS处理网页源代码
    soup = BeautifulSoup(html_doc,'html.parser')

    list = soup.find('div',class_='lst').find_all('a',class_='u-card')
    num=len(list)
    for i in range(num):
        part=list[i].get("href")
        #拼接递进url
        purl="http://www.4399dmw.com"+part
        #二次爬取网页
        resp2=requests.get(url=purl,headers=headers)
        html_doc2=resp2.content.decode("utf-8")
        soup2=BeautifulSoup(html_doc2,'html.parser')
        xihuan=soup2.find_all('div',class_="works__info")[3].find_all('a',class_="works__info-link")
        for a in xihuan:
            print(a.get_text())




    pass


def main():
    spider(1)
    # print("Page"+str(1)+"was saved successfully!\n")
    #
    # print("------------\n"+"芜湖！成功啦！")


if __name__ == '__main__':
    main()

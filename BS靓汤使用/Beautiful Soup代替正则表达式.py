import requests
from bs4 import BeautifulSoup

def main():
    url = "http://www.4399dmw.com/search/dh-1-0-0-0-0-{}-0/"
    headers = {
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1",
        "Referer": "http://www.baidu.com"
    }

    for i in range(1,15):
        ur=url.format(i)
        resp = requests.get(url=ur, headers=headers)
    # 保存页面源代码
        html_doc = resp.content.decode("utf-8")

    # 使用BS处理网页源代码
        soup = BeautifulSoup(html_doc,'html.parser')

    #select使用
        #查找所有div下 id='xxxxxx'的标签内容，放在一个list里
        #print(soup.select("div > #xxxxxxx")[0].get_text())
        #print(soup.select(“ul > .aaa")[1].get_text()) //ul底下class="aaa"的第二个的文本取出来

        #找到class='m-hd'的div标签
        #print(soup.find_all('a', class_='u-card')[0].get_text().strip())
        #get_text() 获取其中文本数据 ； strip() 去除空格、换行

    #取出网页的标题
        #print(soup.title.string)
    #取出所有的img标签，放在一个list里
        #print(soup.find_all("img"))
    #找到所有class='u-tt',无视标签
        #print(soup.find_all(class_='u-tt'))

        list = soup.find('div',class_='lst').find_all('a',class_='u-card')
        for item in list:
            #取出所有list中每一项的细节
            mz=item.find('p',class_='u-tt').get_text()
            #取出图片地址
            src="http:"+item.find('img').get('data-src')
            text=mz+"------"+src
            with open("F:/Py-Pro/Spider/爬虫基础/test/4399动漫--Page"+str(i)+".txt", "a",encoding="utf-8") as f: #'a'表示文本追加
                f.write(text+"\n")

        print("Page%d was saved successfully!"%i)
    print("\n"+"------"+"\n"+"呜呼~舒服了~~")




# #获取页面中有多少个这种元素
#     number=len(soup.find_all('a', class_='u-card'))
#     #print(number)
#     for i in range(number):
#         #获取某个元素的文字内容
#         print(soup.find_all('a',class_='u-card')[i].get_text().strip())

    pass


if __name__ == '__main__':
    main()

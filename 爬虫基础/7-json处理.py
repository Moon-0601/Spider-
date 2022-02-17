import requests
import json
from pprint import pprint




def main():
    url = "http://127.0.0.1/test.json"
    headers={
        "User-Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1",
        "Referer":"http://www.baidu.com"
    }
    resp = requests.get(url=url,headers=headers)
    json_str = resp.content.decode("utf-8")
    #print(json_str)

    # 把字符串变成了字典
    js_dict = json.loads(json_str)
    # # 访问json转化后的字典
    #pprint(js_dict["objects"][1]["EmailAddress"])

    #保存一下
    """
    with open("F:/Py-Pro/Spider/爬虫基础/test/js.txt","w",encoding="utf-8") as f:
        f.write(json.dumps(js_dict,ensure_ascii=False,indent=2))    #ensure_ascii=False 如果有中文，请你显示中文；indent=2 把子节点往后移两个空格
    """

    #读取文件
    with open("F:/Py-Pro/Spider/爬虫基础/test/js.txt","r") as f:
        duqu=json.load(f)
        print(duqu)

    pass


if __name__ == '__main__':
    main()
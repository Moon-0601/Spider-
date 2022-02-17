import requests
from retrying import retry


# 如果失败就请求3次，执行3次如果还失败就报错，可以配合try
@retry(stop_max_attempt_number=3)
def qingqiu(inurl):
    url = inurl
    print("开始请求网站：" + url)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.81 Safari/537.36"
    }
    res = requests.get(url=url, headers=headers)
    with open("F:/Py-Pro/Spider/爬虫基础/test/a.txt", "wb+") as f:
        f.write(res.content)
    print("请求成功!")
    pass


def main():
    try:
        qingqiu("http://www.4399dmw.com/search/dh-1-0-0-0-0-1-0/")
    except:
        print("请求失败了宝!")
    pass


if __name__ == '__main__':
    main()

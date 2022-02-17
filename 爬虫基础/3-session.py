import requests
from  requests import utils


def main():
    url = "http://192.168.152.130/sqli-labs/less-20/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.81 Safari/537.36"

    }
    data = {"uname":"admin", "passwd":"admin"}
    # 实例化session
    session = requests.session()

    # 发送post请求，提交用户名密码
    session.post(url, headers=headers, data=data)

    # 此时session中已经有cookie信息，可以直接用session去get登录后的任何页面
    resp = session.get(url, headers=headers)
    print(resp.content.decode("utf-8"))

    pass


if __name__ == '__main__':
    main()

####直接从返回中获得cookie信息
    # headers = {
    #     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.81 Safari/537.36"
    #
    # }
    # data = {"uname": "admin", "passwd": "admin"｝
    # resp=requests.post(url,headers=headers,data=data)
    # #解码cookie
    # cookies=requests.utils.dict_from_cookiejar(resp.cookies)
    # print(cookies)


####cookie直接登录
    #(1)
    #url = "http://192.168.152.130/sqli-labs/less-20/"
    # headers = {
    #     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.81 Safari/537.36"
    #
    # }
    # cookie_dict = {"uname": "admin"}
    # resp = session.get(url, headers=headers,cookies=cookie_dict)
    # print(resp.content.decode("utf-8"))
    #
    #(2)
    # url = "http://192.168.152.130/sqli-labs/less-20/"
    # headers = {
    #     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.81 Safari/537.36"
    #     "Cookie":"uname=admin"
    # }
    # resp = session.get(url, headers=headers)
    # print(resp.content.decode("utf-8"))
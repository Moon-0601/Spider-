import requests
from  requests import utils


def main():
    url = "http://192.168.152.130/sqli-labs/less-20/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.81 Safari/537.36"

    }
    data = {"uname":"admin", "passwd":"admin"}

#ssl证书问题：不去验证ssl证书
    resp =requests.post(url, headers=headers,data=data,verify=False)
    print(resp.content.decode("utf-8"))

    pass


if __name__ == '__main__':
    main()
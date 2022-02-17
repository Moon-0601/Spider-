# import requests
#
#
# def main():
#     url = "http://www.4399dmw.com/search/dh-1-0-0-0-0-{}-0/"
#     url_list = []
#     headers = {
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.81 Safari/537.36"
#     }
#     for i in range(3):
#         url_list.append(url.format(i))
#
#     p=1
#     for u in url_list:
#         resp = requests.get(url=u, headers=headers)
#         with open("a"+str(p)+".txt", "wb+") as f:
#             f.write(resp.content)
#             p=p+1
#
#     pass
#
#
# if __name__ == '__main__':
#     main()

import requests


def main():
    url = "http://www.4399dmw.com/search/dh-1-0-0-0-0-{}-0/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.81 Safari/537.36"
    }
    for i in range(4):
        ur=url.format(i)
        print(ur)
        resp = requests.get(url=ur, headers=headers)
        with open("a"+str(i)+".txt", "wb+") as f:
            f.write(resp.content)


    pass


if __name__ == '__main__':
    main()


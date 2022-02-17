import random

#User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.81 Safari/537.36

def main():
####User-agent:
    version_id=random.randint(50,100)
    os_type= ['Windows NT 10.0','Windows NT 6.1','linux 10.0']

    ua="Mozilla/5.0 ("+random.choice(os_type)+"; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758."+str(version_id)+" Safari/537.36"

####referer

####cookie
#考虑建立cookie池（多账户）

####通过ip
#使用代理IP等方法

####验证码
#Py机器学习、人工智能、神经网络写程序识别，打码平台

#####自定义字体
# 1.有的网站通过审查元素字体无法显示，显示为口，考虑使用手机网络访问
# 2.通过字体偏移



    pass

if __name__ == '__main__':
    main()
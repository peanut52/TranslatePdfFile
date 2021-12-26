from urllib import request, parse
import ssl
import hashlib
import time
import random
import requests
import json

context = ssl._create_unverified_context()


# you_dao_url = "https://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
# request.Request(you_dao_url)  # 一共4个参数：url,data=None,headers={},method=None
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.57'}


class YouDao:
    def __init__(self, msg):
        self.msg = msg
        self.url = f"http://fanyi.youdao.com/translate?&doctype=json&type=AUTO&i={self.msg}"
        self.D = "ebSeFb%=XZ%T[KZ)c(sy!"
        self.salt = self.get_salt()[0]
        self.its = self.get_salt()[1]
        self.sign = self.get_sign()

    def get_md(self, value):
        """md5加密"""
        m = hashlib.md5()
        # m.update(value)
        m.update(value.encode('utf-8'))
        return m.hexdigest()

    @staticmethod
    def get_salt():
        """根据当前时间戳获取salt参数"""
        salt_value = int(time.time() * 10000)
        return str(salt_value), str(salt_value)[:-1]

    def get_sign(self):
        """使用md5函数和其他参数，得到sign参数"""
        s = "fanyideskweb" + self.msg + self.salt + self.D
        return self.get_md(s)

    def get_result(self):
        """headers里面有一些参数是必须的，注释掉的可以不用带上"""
        headers = {
            'Cookie': 'OUTFOX_SEARCH_USER_ID=-2022895048@10.168.8.76;',
            'Referer': 'http://fanyi.youdao.com/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; rv:51.0) Gecko/20100101 Firefox/51.0',
        }

        my_dic = {
            'i': self.msg,
            'from': 'AUTO',
            'to': 'AUTO',
            'smartresult': 'dict',
            'client': 'fanyideskweb',
            'salt': self.salt,
            'sign': self.sign,
            'lts': self.its,
            'bv': '41b74c13070eef7b03d48873655bdee2',
            'doctype': 'json',
            'version': '2.1',
            'keyfrom': 'fanyi.web',
            'action': 'FY_BY_REALTlME',
            'typoResult': 'true'
        }
        # print(my_dic)
        html = requests.post(self.url, data=my_dic, headers=headers).text
        infos = json.loads(html)
        print(infos)
        if infos.get("translateResult"):
            return infos["translateResult"][0][0]["tgt"]
        return -1
        # data = bytes(parse.urlencode(my_dic), 'utf-8')
        # print(data)
        # print(3)
        # req = request.Request(you_dao_url, data, headers, method='POST')
        # print(req)
        # print(4)
        # response = request.urlopen(req)
        # print(response.read().decode('utf-8'))


if __name__ == '__main__':
    # y = YouDao('你是我的小苹果，我是你的优乐美')
    y = YouDao('You are my little apple, I am your best music beauty')
    print(y.get_result())

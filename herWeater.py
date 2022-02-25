#!/usr/bin/python3
#coding=utf-8

import requests, json
import os

SCKEY=os.environ.get('SCKEY') ##Server酱推送KEY

def ServerPush(info): #Server酱推送
    api = " https://sctapi.ftqq.com/{}.send".format(SCKEY)
    title = "打卡打卡！"
    content = info.replace('\n','\n\n')
    data = {
        "text": title,
        "desp": content
    }
    print(content)
    requests.post(api, data=data)
def main():
    try:
        tdwt = "晴晴，打卡了！"
        ServerPush(tdwt)
    except Exception:
        error = '【出现错误】\n　　今日推送错误，请检查服务或网络状态！'
        print(error)
        print(Exception)

if __name__ == '__main__':
    main()

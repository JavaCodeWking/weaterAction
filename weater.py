#!/usr/bin/python3
#coding=utf-8

import requests, json
import os

SCKEY=os.environ.get('SCKEY')
SKEY=os.environ.get('SKEY')
def MLMPush(info):
    api = " https://sctapi.ftqq.com/{}.send".format(SCKEY)
    title = "该打卡了，晴晴"
    content = info.replace('\n','\n\n')
    data = {
        "text": title,
        "desp": content
    }
    requests.post(api, data=data)

def WQPush(info):
    api = " https://sctapi.ftqq.com/{}.send".format(SKEY)
    title = "该打卡了，晴晴"
    content = info.replace('\n','\n\n')
    data = {
        "text": title,
        "desp": content
    }
    requests.post(api, data=data)

def main():
    try:
        text = "爱你晴晴，记得打卡呀"
        WQPush(text)
        MLMPush(text)
    except Exception:
        error = '【出现错误】\n　　今日推送错误，请检查服务或网络状态！'
        print(error)
        print(Exception)

if __name__ == '__main__':
    main()

# -*- coding: utf-8 -*-
import sys
import time
import itchat
from itchat.content import *
import redis

r=redis.Redis(host='10.252.89.60', port=6379, password='qwqwqwqw')

def _task():
    _ = r.rpop('send:wechat:group')

    if _:
        val = str(_, encoding = "utf-8")
        return val
    return

def main():
    while True:
        task = _task()
        if task:
            #找到UserName
            users = itchat.search_friends(name=u'shrimp')
            userName = users[0]['UserName']
            #然后给他发消息
            itchat.send(task, toUserName = userName)
        else:
            time.sleep(3)

if __name__ == '__main__':
    # 扫二维码登录
    # itchat.auto_login(hotReload=True)
    itchat.auto_login(enableCmdQR=2)
    main()

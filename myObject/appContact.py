#!/usr/bin/env python
# -*- coding:utf-8 -*-
##
 # Copyright (C) 2018 All rights reserved.
 #



import random

from CorpApi import *
from weConf import *

api = CorpApi(TestConf['CORP_ID'], TestConf["APP_SECRET"])

try :
##
    response = api.httpCall(
            CORP_API_TYPE['MESSAGE_SEND'],
        {
            "touser": "hyss_poluo",
            "msgtype": "news",
            "agentid": TestConf["APP_ID"],

            "news" : {
                "articles" : [
                    {
                        "title" : "中秋节礼品领取",
                        "description" : "今年中秋节公司有豪礼相送",
                        "url" : "URL",
                        "picurl" : "http://img4.imgtn.bdimg.com/it/u=3502443110,870820812&fm=26&gp=0.jpg"
                    }
                ]
   },

            "enable_id_trans": 0
        })
    print (response)
    #chatid = response['chatid']
except ApiException as e :
    print (e.errCode, e.errMsg)
    #print('test')

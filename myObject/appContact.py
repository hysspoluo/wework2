#!/usr/bin/env python
# -*- coding:utf-8 -*-
##
 # Copyright (C) 2018 All rights reserved.
 #



import random

from CorpApi import *
from weConf import *

api = CorpApi(TestConf['CORP_ID'], TestConf["CONTACT_SYNC_SECRET"])

try :
##
    response = api.httpCall(
            CORP_API_TYPE['DEPARTMENT_LIST']
    )

    #print (response)
    department = response["department"]
    for item in department:
        print(item["name"],item['parentid'])
    #chatid = response['chatid']
except ApiException as e :
    print (e.errCode, e.errMsg)
    #print('test')

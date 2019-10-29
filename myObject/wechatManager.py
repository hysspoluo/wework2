from CorpApi import *
from weConf import *

"""
CORP_ID,所在单位的ID
CONTACT_SYNC_SECRET，所在应用的SECRET
"""


api = CorpApi(TestConf['CORP_ID'], TestConf["CONTACT_SYNC_SECRET"])

"""
getsortkey()-----部门列表的排序规则
get_department()-----获得部门列表
get_taglist()-----获取标签列表

"""

#####################################
## 获取部门列表
def getSortKey(elem):
    return elem["parentid"]

########################
#获取部门列表
def get_department():
    try:
        response = api.httpCall(
            CORP_API_TYPE['DEPARTMENT_LIST']
        )

        #print (response)
        department = response["department"]
        department_new = []
        for item in department:
            if item["parentid"]  in (5755146,5755148):
                department_new.append(item)
        #print(department_new)
        department_new.sort(key = getSortKey)
        return department_new
    except ApiException as e:
        print(e.errCode, e.errMsg)

####################################
#获取标签列表
def get_taglist():
    try:
        response = api.httpCall(
            CORP_API_TYPE['TAG_GET_LIST']
        )

        taglist = response["taglist"]
        tagnamelist = []
        for item in taglist:
            tagnamelist.append(item["tagname"])

        return (taglist,tagnamelist)

    except ApiException as e:
        print(e.errCode, e.errMsg)
from CorpApi import *
from weConf import *

import re
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


class mywechatmanager():
    def __init__(self):
        self.departmentlist = self.get_department()

    def get_department(self):
        try:
            response = api.httpCall(
                CORP_API_TYPE['DEPARTMENT_LIST']
            )
            department = response["department"]
            department_new = []
            for item in department:
                if item["parentid"] in (5755146, 5755148):
                    department_new.append(item)
            department_new.sort(key=getSortKey)
            return department_new
        except ApiException as e:
            print(e.errCode, e.errMsg)
            return  department_new
#获取部门的ID
    def searchdepartmentID(self,departmentname):
        for item in self.departmentlist:
            if item["name"] == departmentname:
                departmentID = item["id"]
                break
        return departmentID




    def get_taglist(self):
        try:
            response = api.httpCall(
                CORP_API_TYPE['TAG_GET_LIST']
            )
            taglist = response["taglist"]
            tagnamelist = []
            for item in taglist:
                tagnamelist.append(item["tagname"])
            return (taglist, tagnamelist)
        except ApiException as e:
            print(e.errCode, e.errMsg)


    def create_user(self,userInfo,addmailflag):
        #数据初始化
        info =  {
                'userid' : userInfo["wechatID"],
                'name' : userInfo["username"],
                'mobile' : userInfo["phone"],
                'email' : userInfo["mail"],
                'department':[self.searchdepartmentID(userInfo["department"])]
            }
        if addmailflag == 0:
            info["email"] = ""
        #开始处理
        try:
            response = api.httpCall(
                CORP_API_TYPE['USER_CREATE'], info)
            #print(response)
        except ApiException as e:
            response = (e.errCode, e.errMsg)
            response = {"errcode":e.errCode,"errmsg":e.errMsg}
            #print(e.errCode, e.errMsg)
        return response




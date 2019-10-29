# 成员管理
from weConf import *
# 获取Token
from tencent_exmail.Initiative.get_access_token import GetAccessToken
from tencent_exmail.ContactManagement.UserManagement import User
from tencent_exmail.ContactManagement.DepartmentMangement import Department

# 公司ID
CORP_ID = TestConf["MAIL_CORP_ID"]


# 部门管理只需要用到通讯录应用的secret
# 通讯录管理secret
CONTACT_SECRET = TestConf["MAIL_CONTACT_SYNC_SECRET"]




def getToken():
    ex = GetAccessToken(corpid=CORP_ID, corpsecret=CONTACT_SECRET)
    res = ex.get_access_token()
    access_token = res['access_token']
    return access_token

"""
#获取部门
depart = Department(access_token = access_token,operation = "list")
res = depart.list_departs()
#print(res)
"""
def createUser(userInfo)

user = User(access_token = access_token,
                 operation='create',
                 userid='wangdana@tio.org.cn',
                 name='王大拿',
                 department=[24584849607280421],
                 position='',
                 mobile='13959218777',
                 tel='',
                 extid='',
                 gender='1',
                 slaves=[],
                 enable=1,
                 password='Wdn@1234',
                 cpwd_login=1,
                 department_id='',
                 fetch_child=0,
                 userlist='')
res2 = user.create_user()
print(res2)



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


ex = GetAccessToken(corpid=CORP_ID, corpsecret=CONTACT_SECRET)
res = ex.get_access_token()
access_token = res['access_token']
#获取部门
depart = Department(access_token = access_token,operation = "list")
res = depart.list_departs()
print(res)

user = User( access_token,
                 operation,
                 userid='',
                 name='',
                 department='',
                 position='',
                 mobile='',
                 tel='',
                 extid='',
                 gender='',
                 slaves='',
                 enable=1,
                 password='',
                 cpwd_login='',
                 department_id='',
                 fetch_child=0,
                 userlist='')
res2 = user.create_user()
print(res2)


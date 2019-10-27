#from PyQt5 import (QtWidgets)
#from PyQt5.QtWidgets import (QWidget, QApplication,QMainWindow)
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from sys import argv,exit
from CorpApi import *
from weConf import *
from new import Ui_Form
"""
CORP_ID,所在单位的ID
CONTACT_SYNC_SECRET，所在应用的SECRET
"""


api = CorpApi(TestConf['CORP_ID'], TestConf["CONTACT_SYNC_SECRET"])

wechatFlag = 1
mailFlag = 0


"""
getsortkey()-----部门列表的排序规则
get_department()-----获得部门列表
get_taglist()-----获取标签列表

"""

#####################################
## 获取部门列表
def getSortKey(elem):
    return elem["parentid"]

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

#排版布局
def getScreenRect():
    desktop = QApplication.desktop()
    screenRect = desktop.screenGeometry()
    return screenRect

##############################################################
#创建新用户


def create_user(userInfo,self):
    try:
        response = api.httpCall(
            CORP_API_TYPE['USER_CREATE'],userInfo)
        print(response)
    except ApiException as e:
        response = (e.errCode, e.errMsg)
        print(e.errCode, e.errMsg)


    self.textEdit_result.append("----添加结果-----\n"+str(response))



class MainDialog(QWidget,Ui_Form):#重写页面
    def __init__(self,parent = None,title = "企业微信添加用户"):
        super(MainDialog,self).__init__(parent = parent)
        self.setupUi(self)
        self.title = title
        self.setWindowTitle(title)

        self.department = get_department()
        (self.taglist,self.tagnamelist) = get_taglist()

        self.init_tageditline()

        self.init_departmentCombobox()#初始化部门下拉条

        # 设置合适的窗口大小
        screenReck = getScreenRect()
        self.resize(screenReck.width()/2,screenReck.height()/2)

##################################
#初始化部门选择框
    def init_departmentCombobox(self):
        department_list = []
        for item in self.department:
            department_list.append(item["name"])

        for item in department_list:
            self.comboBox_department.addItem(item)

        self.comboBox_department.setCurrentIndex(-1)
        completer = QCompleter(department_list)
        completer.setFilterMode(Qt.MatchContains)
        completer.setCompletionMode(QCompleter.PopupCompletion)
        self.comboBox_department.setCompleter(completer)

#################################
#初始化标签
    def init_tageditline(self):

        completer = QCompleter(self.tagnamelist)
        completer.setFilterMode(Qt.MatchContains)
        completer.setCompletionMode(QCompleter.PopupCompletion)
        self.lineEdit_tag.setCompleter(completer)



    def add_person(self):
        self.textEdit_result.setText("-----开始添加-----")
        ############################################################
        #采集基础信息，为后续添加做准备

        user_name = self.lineEdit_name.text()
        user_phone = self.lineEdit_phone.text()
        user_department = self.comboBox_department.currentText()
        uer_department_id = self.department[self.comboBox_department.currentIndex()]["id"]
        user_id = self.lineEdit_id.text()
        user_tag = self.lineEdit_tag.text()
        user_tag_id = self.taglist[self.tagnamelist.index(user_tag)]["tagid"]
        user_mail = self.lineEdit_mail.text()+"@tio.org.cn"
        user_gender = self.get_gender()
        #生成用户信息
        userInfo = {
            'userid': user_id,
            'name': user_name,
            'gender':user_gender
            'mobile': int(user_phone),
            'tag': user_tag_id,
            'email': 'zhangsan@ipp.cas.cn',
            'department': uer_department_id,
        }



        ##########################################################
        #添加邮箱



        ##########################################################
        #添加企业微信账号



        #create_user(userInfo,self)



    def get_gender(self):
        if self.radioButton_man.isChecked():
            return 1
        else:
            return 0

    def addMailOrNot(self):
        if self.radioButton_yes.isChecked():
            self.lineEdit_mail.setEnabled(True)
        else:
            self.lineEdit_mail.setEnabled(False)

    def addToWechat(self):#加入到企业微信
        if self.checkBox_wechat.isChecked():
            wechatFlag = 1
        else:
            wechatFlag = 0
        print(wechatFlag)
    def addToMail(self):
        if self.checkBox_mail.isChecked():
            mailFlag = 1
            self.lineEdit_mail.setEnabled(True)
        else:
            mailFlag = 0
            self.lineEdit_mail.setEnabled(False)
            self.lineEdit_mail.clear()

if __name__ == "__main__":
    app = QApplication(argv)
    mainWindow = MainDialog()
    #初始化数据
    #获取部门列表


    mainWindow.show()


    exit(app.exec_())
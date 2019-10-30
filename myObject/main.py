#from PyQt5 import (QtWidgets)
#from PyQt5.QtWidgets import (QWidget, QApplication,QMainWindow)
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from sys import argv,exit
#from CorpApi import *
#from weConf import *
#from wechatManager import *
#from mailManager import *
from new import Ui_Form

from myObject.mailManager import mymailmanager
from myObject.wechatManager import  mywechatmanager

userInfo={
    "username":"",
    "gender":1,
    "department":"",
    "phone":"",
    "wechatID":"",
    "wechatTag":"",
    "mail":"",
}


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
        #print(response)
    except ApiException as e:
        response = (e.errCode, e.errMsg)
        #print(e.errCode, e.errMsg)


    self.textEdit_result.append("----添加结果-----\n"+str(response))



class MainDialog(QWidget,Ui_Form):#重写页面
    def __init__(self,parent = None,title = "企业微信-企业邮箱账号管理"):
        super(MainDialog,self).__init__(parent = parent)
        self.setupUi(self)
        self.title = title
        self.wechatFlag = 1
        self.mailFlag = 0
        self.addMailToWechat = 1
        self.setWindowTitle(title)
        self.mailManager = mymailmanager()
        self.wechatManager = mywechatmanager()
        self.department = self.wechatManager.departmentlist
        (self.taglist,self.tagnamelist) = self.wechatManager.get_taglist()
        self.init_tageditline()
        self.init_departmentCombobox()#初始化部门下拉条
        #电话号码正则表达式
        my_regex = QRegExp("^[1]([3-9])[0-9]{9}$")
        my_validator = QRegExpValidator(my_regex,self.lineEdit_phone)
        self.lineEdit_phone.setValidator(my_validator)
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

    def setUserInfo(self):
        userInfo["username"] = self.lineEdit_name.text()
        userInfo["phone"] = self.lineEdit_phone.text()
        userInfo["department"] = self.comboBox_department.currentText()
       # uer_department_id = self.department[self.comboBox_department.currentIndex()]["id"]
       # userInfo["department_id"] = uer_department_id
        userInfo["wechatID"] = self.lineEdit_id.text()
        userInfo["wechatTag"] = self.lineEdit_tag.text()
        #user_tag_id = self.taglist[self.tagnamelist.index(user_tag)]["tagid"]
        userInfo["mail"] = self.lineEdit_mail.text() + "@tio.org.cn"
        userInfo["gender"] = self.get_gender()


    def add_person(self):
        self.textEdit_result.clear()
        if self.mailFlag == 0 and self.wechatFlag ==0:
            self.textEdit_result.setText("请选择需要开通的账号----------\n")
            return
        self.textEdit_result.setText("开始添加----------\n")
        ############################################################
        #采集基础信息，为后续添加做准备
        self.setUserInfo()
        #开通邮箱
        if self.mailFlag == 1:
            self.textEdit_result.append("开始开通邮箱账户----------")
            mail_result = self.mailManager.createUser(userInfo)
            if mail_result["errcode"] == 0:
                self.textEdit_result.append("----------邮箱开通成功----------\n")
            else:
                self.textEdit_result.append("邮箱开通失败，失败原因："+mail_result["errmsg"]+"\n")
                self.addMailToWechat = 0
        #开通企业微信
        if self.wechatFlag == 1:
            self.textEdit_result.append("开始开通企业微信----------")
            wechat_result = self.wechatManager.create_user(userInfo,self.addMailToWechat)
            if wechat_result["errcode"] == 0:
                self.textEdit_result.append("----------开通成功----------\n")
            else:
                self.textEdit_result.append("开通失败，失败原因："+wechat_result["errmsg"]+"\n")




        #create_user(userInfo,self)



    def get_gender(self):
        if self.radioButton_man.isChecked():
            return 1 #男性
        else:
            return 2  #女性

    def addMailOrNot(self):
        if self.radioButton_yes.isChecked():
            self.lineEdit_mail.setEnabled(True)
        else:
            self.lineEdit_mail.setEnabled(False)

    def addToWechat(self):#加入到企业微信
        if self.checkBox_wechat.isChecked():
            self.wechatFlag = 1
        else:
            self.wechatFlag = 0
    def addToMail(self):
        if self.checkBox_mail.isChecked():
            self.mailFlag = 1
            #self.lineEdit_mail.setEnabled(True)
        else:
            self.mailFlag = 0
            #self.lineEdit_mail.setEnabled(False)
            #self.lineEdit_mail.clear()

if __name__ == "__main__":
    app = QApplication(argv)
    mainWindow = MainDialog()
    #初始化数据
    #获取部门列表
    mainWindow.show()
    exit(app.exec_())
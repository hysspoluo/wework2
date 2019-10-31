#from PyQt5 import (QtWidgets)
#from PyQt5.QtWidgets import (QWidget, QApplication,QMainWindow)
import re
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
        #开始转换
        self.textEdit_result.setText("开始----------\n开户姓名："+self.lineEdit_name.text())
        #进行格式校验
        result = self.checkingformat()
        if result["errcode"] == 0:
            self.textEdit_result.setText("格式校验完成，开始添加-------")
        else:
            self.textEdit_result.setText(result["errMsg"])
            return
        ############################################################
        #采集基础信息，为后续添加做准备
        self.setUserInfo()
        #开通邮箱
        if self.mailFlag == 1:
            self.textEdit_result.append("邮箱账户创建----------")
            mail_result = self.mailManager.createUser(userInfo)
            if mail_result["errcode"] == 0:
                self.textEdit_result.append("----------邮箱开通成功----------\n账户名："+userInfo["mail"]+"\t初始密码：Test@1234")
            else:
                self.textEdit_result.append("邮箱开通失败，失败原因："+mail_result["errmsg"]+"\n")
                self.addMailToWechat = 0
        self.textEdit_result.append("--------------------------------------\n")
        #开通企业微信
        if self.wechatFlag == 1:
            self.textEdit_result.append("企业微信账户创建----------")
            wechat_result = self.wechatManager.create_user(userInfo,self.addMailToWechat)
            if wechat_result["errcode"] == 0:
                self.textEdit_result.append("----------创建成功----------\n"+"账户名："+userInfo["wechatID"])
            else:
                self.textEdit_result.append("创建失败，失败原因："+wechat_result["errmsg"]+"\n")



    def checkingformat(self):
        name = userInfo["username"]
        department = userInfo["department"]
        phone = userInfo["phone"]
        wechatid = userInfo["wechatID"]
        wechatTag = userInfo["wechatTag"]
        mail = userInfo["mail"]
        #正则表达式公式
        # 邮箱
        pattern_mail = re.compile(r'\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*')
        # ID
        pattern_userid = re.compile(r'^[a-zA-Z][a-zA-Z0-9_]{4,16}$')
        # 姓名
        pattern_name = re.compile(r'^([\u4e00-\u9fa5]{2,20}|[a-zA-Z.\s]{2,20})$')
        # 电话
        pattern_phone = re.compile(r'1\d{10}')
        if re.match(pattern_name,name) == None:
            errMsg = "姓名格式错误，请检查"
            error = -1
        elif re.match(pattern_phone,phone) == None:
            errMsg = "电话格式错误，请检查"
            error = -1
        elif re.match(pattern_mail,mail) == None:
            errMsg = "邮件格式有误，请检查"
            error = -1
        elif re.match(pattern_userid,wechatid) == None:
            errMsg = "企业微信账号格式有误，请检查"
            error = -1
        #elif department not in self.departmentname:
        #   errMsg = "部门名称错误，请重新选择"
        #    error = -1
        elif wechatTag not in self.tagnamelist:
            errMsg = "标签错误，请重新选择"
            error = -1
        else:
            errMsg = "输入格式正确"
            error = 0
        res = {{"errcode":error,"errmsg":errMsg}}
        return res



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
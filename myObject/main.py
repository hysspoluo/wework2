from PyQt5 import (QtWidgets)
from PyQt5.QtWidgets import (QWidget, QApplication,QMainWindow)

from sys import argv,exit
from CorpApi import *
from weConf import *

from new import Ui_Form

api = CorpApi(TestConf['CORP_ID'], TestConf["CONTACT_SYNC_SECRET"])

"""
获取列表
getsortkey()-----部门列表的排序规则
get_department()-----获得部门列表
"""

#获取部门列表
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

#排版布局
def getScreenRect():
    desktop = QApplication.desktop()
    screenRect = desktop.screenGeometry()
    return screenRect



class MainDialog(QWidget,Ui_Form):#重写页面
    def __init__(self,parent = None,title = "企业微信添加用户"):
        super(MainDialog,self).__init__(parent = parent)
        self.setupUi(self)
        self.title = title
        self.setWindowTitle(title)

        department = get_department()
        for item in department:
            self.comboBox_department.addItem(item["name"])
        #设置合适的窗口大小
        screenReck = getScreenRect()
        self.resize(screenReck.width()/2,screenReck.height()/2)


    def add_person(self):

        user_name = self.lineEdit_name.text()
        user_phone = self.lineEdit_phone.text()
        #user_department = self.comboBox_department.text()
        user_id = self.lineEdit_id.text()
        user_tag = self.lineEdit_tag.text()
        user_mail = self.lineEdit_mail.text()+"@tio.org.cn"
        user_gender = self.get_gender()
        mailFlag = self.get_mailFlag()

        print(user_name,user_phone,user_id,user_tag,user_mail,user_gender,mailFlag)


    def get_gender(self):
        if self.radioButton_man.isChecked():
            return "男"
        else:
            return "女"
    def get_mailFlag(self):
        if self.radioButton_yes.isChecked():
            return 1
        else:
            return 0





if __name__ == "__main__":
    app = QApplication(argv)
    mainWindow = MainDialog()

    #初始化数据
    #获取部门列表


    mainWindow.show()


    exit(app.exec_())
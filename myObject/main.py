from PyQt5 import (QtWidgets)
from PyQt5.QtWidgets import (QWidget, QApplication,QMainWindow)

from sys import argv,exit
from CorpApi import *
from weConf import *

from new import Ui_Form

api = CorpApi(TestConf['CORP_ID'], TestConf["CONTACT_SYNC_SECRET"])
def get_department():
    try:
        response = api.httpCall(
            CORP_API_TYPE['DEPARTMENT_LIST']
        )

        #print (response)
        department = response["department"]
        print(len(department))
        #print(department)
        for item in department:

            if item["parentid"] not in [5755148,5755146]:
                department.remove(item)
        print(len(department))
        #    print(item["name"], item['parentid'])
        # chatid = response['chatid']
    except ApiException as e:

        print(e.errCode, e.errMsg)
        # print('test')

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
    get_department()
    #初始化数据
    #获取部门列表


    mainWindow.show()


    exit(app.exec_())
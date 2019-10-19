from PyQt5 import (QtWidgets)
from PyQt5.QtWidgets import (QWidget, QApplication)
from userManager import Ui_Dialog
from sys import argv,exit
from CorpApi import *
from weConf import *
from test import Ui_Form

api = CorpApi(TestConf['CORP_ID'], TestConf["CONTACT_SYNC_SECRET"])
def get_department():
    try:
        response = api.httpCall(
            CORP_API_TYPE['DEPARTMENT_LIST']
        )

        # print (response)
        #department = response["department"]
        #for item in department:
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



class MainDialog(QWidget,Ui_Dialog):
    def __init__(self,parent = None,title = "企业微信添加用户"):
        super(MainDialog,self).__init__(parent = parent)
        self.setupUi(self)
        self.title = title
        self.setWindowTitle(title)
        #设置合适的窗口大小
        screenReck = getScreenRect()
        self.resize(screenReck.width()/2,screenReck.height()/2)


    def addPerson(self):
        user_name = self.lineEdit.text()
        user_id = self.lineEdit_2.text()
        user_mobile = self.lineEdit_3.text()
        user_gender = self.get_gender()
        print(user_gender)

    def get_gender(self):
        if self.radioButton.isChecked():
            return "男"
        else:
            return "女"






if __name__ == "__main__":
    app = QApplication(argv)
    mainWindow = MainDialog()

    #mainWindow = Ui_Form()
    mainWindow.show()
    exit(app.exec_())
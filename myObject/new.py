# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(634, 445)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(Form)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_phone = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_phone.sizePolicy().hasHeightForWidth())
        self.label_phone.setSizePolicy(sizePolicy)
        self.label_phone.setMinimumSize(QtCore.QSize(55, 0))
        self.label_phone.setMaximumSize(QtCore.QSize(55, 16777215))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        self.label_phone.setFont(font)
        self.label_phone.setAlignment(QtCore.Qt.AlignCenter)
        self.label_phone.setObjectName("label_phone")
        self.horizontalLayout_3.addWidget(self.label_phone)
        self.lineEdit_phone = QtWidgets.QLineEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_phone.sizePolicy().hasHeightForWidth())
        self.lineEdit_phone.setSizePolicy(sizePolicy)
        self.lineEdit_phone.setMinimumSize(QtCore.QSize(180, 0))
        self.lineEdit_phone.setMaximumSize(QtCore.QSize(180, 16777215))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        self.lineEdit_phone.setFont(font)
        self.lineEdit_phone.setObjectName("lineEdit_phone")
        self.horizontalLayout_3.addWidget(self.lineEdit_phone)
        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 1, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_department = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_department.sizePolicy().hasHeightForWidth())
        self.label_department.setSizePolicy(sizePolicy)
        self.label_department.setMinimumSize(QtCore.QSize(75, 0))
        self.label_department.setMaximumSize(QtCore.QSize(75, 16777215))
        self.label_department.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_department.setObjectName("label_department")
        self.horizontalLayout_4.addWidget(self.label_department)
        self.comboBox_department = QtWidgets.QComboBox(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_department.sizePolicy().hasHeightForWidth())
        self.comboBox_department.setSizePolicy(sizePolicy)
        self.comboBox_department.setMinimumSize(QtCore.QSize(220, 0))
        self.comboBox_department.setMaximumSize(QtCore.QSize(220, 16777215))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        self.comboBox_department.setFont(font)
        self.comboBox_department.setEditable(True)
        self.comboBox_department.setObjectName("comboBox_department")
        self.horizontalLayout_4.addWidget(self.comboBox_department)
        self.gridLayout.addLayout(self.horizontalLayout_4, 1, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_sex = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_sex.sizePolicy().hasHeightForWidth())
        self.label_sex.setSizePolicy(sizePolicy)
        self.label_sex.setMinimumSize(QtCore.QSize(55, 0))
        self.label_sex.setMaximumSize(QtCore.QSize(55, 16777215))
        self.label_sex.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_sex.setObjectName("label_sex")
        self.horizontalLayout_2.addWidget(self.label_sex)
        self.radioButton_man = QtWidgets.QRadioButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radioButton_man.sizePolicy().hasHeightForWidth())
        self.radioButton_man.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        self.radioButton_man.setFont(font)
        self.radioButton_man.setChecked(True)
        self.radioButton_man.setObjectName("radioButton_man")
        self.horizontalLayout_2.addWidget(self.radioButton_man)
        self.radioButton_woman = QtWidgets.QRadioButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radioButton_woman.sizePolicy().hasHeightForWidth())
        self.radioButton_woman.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        self.radioButton_woman.setFont(font)
        self.radioButton_woman.setObjectName("radioButton_woman")
        self.horizontalLayout_2.addWidget(self.radioButton_woman)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 1, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_name = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_name.sizePolicy().hasHeightForWidth())
        self.label_name.setSizePolicy(sizePolicy)
        self.label_name.setMinimumSize(QtCore.QSize(75, 0))
        self.label_name.setMaximumSize(QtCore.QSize(75, 16777215))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        self.label_name.setFont(font)
        self.label_name.setAlignment(QtCore.Qt.AlignCenter)
        self.label_name.setObjectName("label_name")
        self.horizontalLayout.addWidget(self.label_name)
        self.lineEdit_name = QtWidgets.QLineEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_name.sizePolicy().hasHeightForWidth())
        self.lineEdit_name.setSizePolicy(sizePolicy)
        self.lineEdit_name.setMinimumSize(QtCore.QSize(220, 0))
        self.lineEdit_name.setMaximumSize(QtCore.QSize(220, 16777215))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        self.lineEdit_name.setFont(font)
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.horizontalLayout.addWidget(self.lineEdit_name)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_id = QtWidgets.QLabel(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_id.sizePolicy().hasHeightForWidth())
        self.label_id.setSizePolicy(sizePolicy)
        self.label_id.setMinimumSize(QtCore.QSize(75, 0))
        self.label_id.setMaximumSize(QtCore.QSize(75, 16777215))
        self.label_id.setAlignment(QtCore.Qt.AlignCenter)
        self.label_id.setObjectName("label_id")
        self.horizontalLayout_5.addWidget(self.label_id)
        self.lineEdit_id = QtWidgets.QLineEdit(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_id.sizePolicy().hasHeightForWidth())
        self.lineEdit_id.setSizePolicy(sizePolicy)
        self.lineEdit_id.setMinimumSize(QtCore.QSize(180, 0))
        self.lineEdit_id.setMaximumSize(QtCore.QSize(180, 16777215))
        self.lineEdit_id.setObjectName("lineEdit_id")
        self.horizontalLayout_5.addWidget(self.lineEdit_id)
        self.gridLayout_2.addLayout(self.horizontalLayout_5, 0, 0, 1, 1)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_tag = QtWidgets.QLabel(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_tag.sizePolicy().hasHeightForWidth())
        self.label_tag.setSizePolicy(sizePolicy)
        self.label_tag.setMinimumSize(QtCore.QSize(75, 0))
        self.label_tag.setMaximumSize(QtCore.QSize(75, 16777215))
        self.label_tag.setAlignment(QtCore.Qt.AlignCenter)
        self.label_tag.setObjectName("label_tag")
        self.horizontalLayout_8.addWidget(self.label_tag)
        self.lineEdit_tag = QtWidgets.QLineEdit(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_tag.sizePolicy().hasHeightForWidth())
        self.lineEdit_tag.setSizePolicy(sizePolicy)
        self.lineEdit_tag.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit_tag.setObjectName("lineEdit_tag")
        self.horizontalLayout_8.addWidget(self.lineEdit_tag)
        self.toolButton_tag = QtWidgets.QToolButton(self.groupBox_2)
        self.toolButton_tag.setObjectName("toolButton_tag")
        self.horizontalLayout_8.addWidget(self.toolButton_tag)
        self.gridLayout_2.addLayout(self.horizontalLayout_8, 0, 1, 1, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.checkBox_wechat = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_wechat.setChecked(True)
        self.checkBox_wechat.setObjectName("checkBox_wechat")
        self.horizontalLayout_7.addWidget(self.checkBox_wechat)
        self.checkBox_mail = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_mail.setObjectName("checkBox_mail")
        self.horizontalLayout_7.addWidget(self.checkBox_mail)
        self.gridLayout_2.addLayout(self.horizontalLayout_7, 1, 0, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.lineEdit_mail = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_mail.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_mail.sizePolicy().hasHeightForWidth())
        self.lineEdit_mail.setSizePolicy(sizePolicy)
        self.lineEdit_mail.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_mail.setObjectName("lineEdit_mail")
        self.horizontalLayout_6.addWidget(self.lineEdit_mail)
        self.label_mail_2 = QtWidgets.QLabel(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_mail_2.sizePolicy().hasHeightForWidth())
        self.label_mail_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.label_mail_2.setFont(font)
        self.label_mail_2.setObjectName("label_mail_2")
        self.horizontalLayout_6.addWidget(self.label_mail_2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.gridLayout_2.addLayout(self.horizontalLayout_6, 1, 1, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.groupBox_3 = QtWidgets.QGroupBox(Form)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.textEdit_result = QtWidgets.QTextEdit(self.groupBox_3)
        self.textEdit_result.setObjectName("textEdit_result")
        self.horizontalLayout_9.addWidget(self.textEdit_result)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton_add = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_add.setObjectName("pushButton_add")
        self.verticalLayout_2.addWidget(self.pushButton_add)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.pushButton = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_2.addWidget(self.pushButton)
        self.horizontalLayout_9.addLayout(self.verticalLayout_2)
        self.verticalLayout.addWidget(self.groupBox_3)

        self.retranslateUi(Form)
        self.pushButton_add.clicked.connect(Form.add_person)
        self.pushButton.clicked.connect(Form.close)
        self.checkBox_wechat.clicked.connect(Form.addToWechat)
        self.checkBox_mail.clicked.connect(Form.addToMail)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBox.setTitle(_translate("Form", "基本信息"))
        self.label_phone.setText(_translate("Form", "手机号:"))
        self.label_department.setText(_translate("Form", "所在部门："))
        self.label_sex.setText(_translate("Form", "性别："))
        self.radioButton_man.setText(_translate("Form", "男"))
        self.radioButton_woman.setText(_translate("Form", "女"))
        self.label_name.setText(_translate("Form", "姓 名："))
        self.groupBox_2.setTitle(_translate("Form", "设置信息"))
        self.label_id.setText(_translate("Form", "账号："))
        self.label_tag.setText(_translate("Form", "标签："))
        self.toolButton_tag.setText(_translate("Form", "..."))
        self.checkBox_wechat.setText(_translate("Form", "企业微信"))
        self.checkBox_mail.setText(_translate("Form", "企业邮箱"))
        self.label_mail_2.setText(_translate("Form", "@tio.org.cn"))
        self.groupBox_3.setTitle(_translate("Form", "结果"))
        self.pushButton_add.setText(_translate("Form", "确认添加"))
        self.pushButton.setText(_translate("Form", "关闭"))


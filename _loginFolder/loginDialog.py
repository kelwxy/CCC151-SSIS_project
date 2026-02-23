from PyQt6 import QtCore, QtGui, QtWidgets

class login_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("LoginDialog")
        Dialog.resize(400, 300)
        Dialog.setMinimumSize(QtCore.QSize(400, 300))
        Dialog.setMaximumSize(QtCore.QSize(400, 300))

        self.gridLayout = QtWidgets.QGridLayout(Dialog)

        # Title
        self.title_label = QtWidgets.QLabel(parent=Dialog)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.title_label.setFont(font)
        self.title_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.gridLayout.addWidget(self.title_label, 0, 0, 1, 2)

        # Line
        self.line = QtWidgets.QFrame(parent=Dialog)
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.gridLayout.addWidget(self.line, 1, 0, 1, 2)

        # Username
        self.username_label = QtWidgets.QLabel(parent=Dialog)
        font2 = QtGui.QFont()
        font2.setPointSize(10)
        font2.setBold(True)
        self.username_label.setFont(font2)
        self.gridLayout.addWidget(self.username_label, 2, 0, 1, 1)

        self.username_input = QtWidgets.QLineEdit(parent=Dialog)
        self.username_input.setMinimumSize(QtCore.QSize(0, 35))
        font3 = QtGui.QFont()
        font3.setPointSize(10)
        self.username_input.setFont(font3)
        self.gridLayout.addWidget(self.username_input, 2, 1, 1, 1)

        # Password
        self.password_label = QtWidgets.QLabel(parent=Dialog)
        self.password_label.setFont(font2)
        self.gridLayout.addWidget(self.password_label, 3, 0, 1, 1)

        self.password_input = QtWidgets.QLineEdit(parent=Dialog)
        self.password_input.setMinimumSize(QtCore.QSize(0, 35))
        self.password_input.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.password_input.setFont(font3)
        self.gridLayout.addWidget(self.password_input, 3, 1, 1, 1)

        # Role ComboBox
        self.role_label = QtWidgets.QLabel(parent=Dialog)
        self.role_label.setFont(font2)
        self.gridLayout.addWidget(self.role_label, 4, 0, 1, 1)

        self.role_comboBox = QtWidgets.QComboBox(parent=Dialog)
        self.role_comboBox.setMinimumSize(QtCore.QSize(0, 35))
        self.role_comboBox.setFont(font3)
        self.role_comboBox.addItems(["User", "Admin"])
        self.gridLayout.addWidget(self.role_comboBox, 4, 1, 1, 1)

        # Error label
        self.error_label = QtWidgets.QLabel(parent=Dialog)
        self.error_label.setStyleSheet("color: red;")
        self.error_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.error_label.setText("")
        self.gridLayout.addWidget(self.error_label, 5, 0, 1, 2)

        # Login Button
        self.login_button = QtWidgets.QPushButton(parent=Dialog)
        self.login_button.setMinimumSize(QtCore.QSize(0, 40))
        font4 = QtGui.QFont()
        font4.setPointSize(11)
        font4.setBold(True)
        self.login_button.setFont(font4)
        self.gridLayout.addWidget(self.login_button, 6, 0, 1, 2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("LoginDialog", "Login"))
        self.title_label.setText(_translate("LoginDialog", "KELWXY login"))
        self.username_label.setText(_translate("LoginDialog", "Username"))
        self.password_label.setText(_translate("LoginDialog", "Password"))
        self.role_label.setText(_translate("LoginDialog", "Role"))
        self.login_button.setText(_translate("LoginDialog", "Login"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = login_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
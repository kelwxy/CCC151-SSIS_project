from PyQt6 import QtCore, QtGui, QtWidgets


class update_College(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(558, 272)
        Dialog.setMinimumSize(QtCore.QSize(558, 272))

        self.widget = QtWidgets.QWidget(parent=Dialog)
        self.widget.setGeometry(QtCore.QRect(9, 9, 541, 253))
        self.widget.setMinimumSize(QtCore.QSize(541, 253))

        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)

        # ===== Title =====
        self.widget_5 = QtWidgets.QWidget(parent=self.widget)
        self.gridLayout_3 = QtWidgets.QGridLayout(self.widget_5)

        self.AddCollege_text = QtWidgets.QLabel(parent=self.widget_5)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.AddCollege_text.setFont(font)

        self.gridLayout_3.addWidget(self.AddCollege_text, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(
            377, 20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum
        )
        self.gridLayout_3.addItem(spacerItem, 0, 1, 1, 1)

        self.gridLayout_2.addWidget(self.widget_5, 0, 0, 1, 1)

        # ===== Line =====
        self.line = QtWidgets.QFrame(parent=self.widget)
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.gridLayout_2.addWidget(self.line, 1, 0, 1, 1)

        # ===== College Code =====
        self.widget_2 = QtWidgets.QWidget(parent=self.widget)
        self.gridLayout = QtWidgets.QGridLayout(self.widget_2)

        self.college_code_text = QtWidgets.QLabel(parent=self.widget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.college_code_text.setFont(font)

        self.college_code_input = QtWidgets.QLineEdit(parent=self.widget_2)
        self.college_code_input.setMinimumSize(QtCore.QSize(101, 41))
        self.college_code_input.setMaximumSize(QtCore.QSize(111, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.college_code_input.setFont(font)

        self.gridLayout.addWidget(self.college_code_text, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.college_code_input, 0, 1, 1, 1)

        spacerItem1 = QtWidgets.QSpacerItem(
            268, 20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum
        )
        self.gridLayout.addItem(spacerItem1, 0, 2, 1, 1)

        self.gridLayout_2.addWidget(self.widget_2, 2, 0, 1, 1)

        # ===== College Name =====
        self.widget_3 = QtWidgets.QWidget(parent=self.widget)
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_3)

        self.college_name_text = QtWidgets.QLabel(parent=self.widget_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.college_name_text.setFont(font)

        self.college_name_input = QtWidgets.QLineEdit(parent=self.widget_3)
        self.college_name_input.setMinimumSize(QtCore.QSize(311, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.college_name_input.setFont(font)

        self.horizontalLayout.addWidget(self.college_name_text)
        self.horizontalLayout.addWidget(self.college_name_input)

        self.gridLayout_2.addWidget(self.widget_3, 3, 0, 1, 1)

        # ===== Buttons =====
        self.widget_4 = QtWidgets.QWidget(parent=self.widget)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_4)

        spacerItem2 = QtWidgets.QSpacerItem(
            95, 20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum
        )
        self.horizontalLayout_2.addItem(spacerItem2)

        self.Save_button = QtWidgets.QPushButton(parent=self.widget_4)
        self.Save_button.setMinimumSize(QtCore.QSize(93, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Save_button.setFont(font)

        self.horizontalLayout_2.addWidget(self.Save_button)

        spacerItem3 = QtWidgets.QSpacerItem(
            96, 20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum
        )
        self.horizontalLayout_2.addItem(spacerItem3)

        self.Cancel_button = QtWidgets.QPushButton(parent=self.widget_4)
        self.Cancel_button.setMinimumSize(QtCore.QSize(93, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Cancel_button.setFont(font)

        self.horizontalLayout_2.addWidget(self.Cancel_button)

        spacerItem4 = QtWidgets.QSpacerItem(
            95, 20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum
        )
        self.horizontalLayout_2.addItem(spacerItem4)

        self.gridLayout_2.addWidget(self.widget_4, 4, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Update College"))
        self.AddCollege_text.setText(_translate("Dialog", "Update College"))
        self.college_code_text.setText(_translate("Dialog", "College Code"))
        self.college_name_text.setText(_translate("Dialog", "College Name"))
        self.Save_button.setText(_translate("Dialog", "Save"))
        self.Cancel_button.setText(_translate("Dialog", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = update_College()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
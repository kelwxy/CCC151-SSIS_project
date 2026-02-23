from PyQt6 import QtCore, QtGui, QtWidgets


class update_Program(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(540, 336)
        Dialog.setMinimumSize(QtCore.QSize(540, 336))

        self.gridLayout_2 = QtWidgets.QGridLayout(Dialog)

        self.widget = QtWidgets.QWidget(parent=Dialog)
        self.widget.setMinimumSize(QtCore.QSize(521, 318))
        self.gridLayout = QtWidgets.QGridLayout(self.widget)

        # ===== Title =====
        self.widget_2 = QtWidgets.QWidget(parent=self.widget)
        self.gridLayout_3 = QtWidgets.QGridLayout(self.widget_2)

        self.add_program_text = QtWidgets.QLabel(parent=self.widget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.add_program_text.setFont(font)

        self.gridLayout_3.addWidget(self.add_program_text, 0, 0, 1, 1)

        spacerItem = QtWidgets.QSpacerItem(
            345, 20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum
        )
        self.gridLayout_3.addItem(spacerItem, 0, 1, 1, 1)

        self.gridLayout.addWidget(self.widget_2, 0, 0, 1, 1)

        # ===== Line =====
        self.line = QtWidgets.QFrame(parent=self.widget)
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.gridLayout.addWidget(self.line, 1, 0, 1, 1)

        # ===== Program Code =====
        self.widget_3 = QtWidgets.QWidget(parent=self.widget)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_3)

        self.program_code_text = QtWidgets.QLabel(parent=self.widget_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.program_code_text.setFont(font)

        self.program_code_input = QtWidgets.QLineEdit(parent=self.widget_3)
        self.program_code_input.setMinimumSize(QtCore.QSize(171, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.program_code_input.setFont(font)

        self.horizontalLayout_2.addWidget(self.program_code_text)
        self.horizontalLayout_2.addWidget(self.program_code_input)

        self.gridLayout.addWidget(self.widget_3, 2, 0, 1, 1)

        # ===== Program Name =====
        self.widget_4 = QtWidgets.QWidget(parent=self.widget)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_4)

        self.program_name_text = QtWidgets.QLabel(parent=self.widget_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.program_name_text.setFont(font)

        self.program_name_input = QtWidgets.QLineEdit(parent=self.widget_4)
        self.program_name_input.setMinimumSize(QtCore.QSize(291, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.program_name_input.setFont(font)

        self.horizontalLayout_3.addWidget(self.program_name_text)
        self.horizontalLayout_3.addWidget(self.program_name_input)

        self.gridLayout.addWidget(self.widget_4, 3, 0, 1, 1)

        # ===== College Code =====
        self.widget_5 = QtWidgets.QWidget(parent=self.widget)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_5)

        self.college_code_text = QtWidgets.QLabel(parent=self.widget_5)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.college_code_text.setFont(font)

        self.college_code_input_comboBox = QtWidgets.QComboBox(parent=self.widget_5)
        self.college_code_input_comboBox.setMinimumSize(QtCore.QSize(141, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.college_code_input_comboBox.setFont(font)

        self.horizontalLayout_4.addWidget(self.college_code_text)
        self.horizontalLayout_4.addWidget(self.college_code_input_comboBox)

        spacerItem1 = QtWidgets.QSpacerItem(
            219, 20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum
        )
        self.horizontalLayout_4.addItem(spacerItem1)

        self.gridLayout.addWidget(self.widget_5, 4, 0, 1, 1)

        # ===== Buttons =====
        self.widget_6 = QtWidgets.QWidget(parent=self.widget)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget_6)

        spacerItem2 = QtWidgets.QSpacerItem(
            89, 20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum
        )
        self.horizontalLayout_5.addItem(spacerItem2)

        self.Save_button = QtWidgets.QPushButton(parent=self.widget_6)
        self.Save_button.setMinimumSize(QtCore.QSize(93, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Save_button.setFont(font)

        self.horizontalLayout_5.addWidget(self.Save_button)

        spacerItem3 = QtWidgets.QSpacerItem(
            89, 20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum
        )
        self.horizontalLayout_5.addItem(spacerItem3)

        self.Cancel_button = QtWidgets.QPushButton(parent=self.widget_6)
        self.Cancel_button.setMinimumSize(QtCore.QSize(93, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Cancel_button.setFont(font)

        self.horizontalLayout_5.addWidget(self.Cancel_button)

        spacerItem4 = QtWidgets.QSpacerItem(
            40, 20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum
        )
        self.horizontalLayout_5.addItem(spacerItem4)

        self.gridLayout.addWidget(self.widget_6, 5, 0, 1, 1)

        self.gridLayout_2.addWidget(self.widget, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Update Program"))
        self.add_program_text.setText(_translate("Dialog", "Update Program"))
        self.program_code_text.setText(_translate("Dialog", "Program Code"))
        self.program_name_text.setText(_translate("Dialog", "Program Name"))
        self.college_code_text.setText(_translate("Dialog", "College Code"))
        self.Save_button.setText(_translate("Dialog", "Save"))
        self.Cancel_button.setText(_translate("Dialog", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = update_Program()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
from PyQt6 import QtCore, QtGui, QtWidgets


class add_Student(object):
    def setupUi(self, AddStudent_Dialog):
        AddStudent_Dialog.setObjectName("AddStudent_Dialog")
        AddStudent_Dialog.resize(500, 532)
        AddStudent_Dialog.setMinimumSize(QtCore.QSize(500, 532))

        self.gridLayout_2 = QtWidgets.QGridLayout(AddStudent_Dialog)

        self.widget = QtWidgets.QWidget(parent=AddStudent_Dialog)
        self.widget.setMinimumSize(QtCore.QSize(481, 513))
        self.gridLayout = QtWidgets.QGridLayout(self.widget)

        # Title
        self.widget_3 = QtWidgets.QWidget(parent=self.widget)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_3)

        self.Edit_Student_text = QtWidgets.QLabel(parent=self.widget_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.Edit_Student_text.setFont(font)
        self.horizontalLayout_2.addWidget(self.Edit_Student_text)

        spacerItem = QtWidgets.QSpacerItem(
            40, 20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum
        )
        self.horizontalLayout_2.addItem(spacerItem)

        self.gridLayout.addWidget(self.widget_3, 0, 0, 1, 1)

        # Line
        self.line = QtWidgets.QFrame(parent=self.widget)
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.gridLayout.addWidget(self.line, 1, 0, 1, 1)

        # ID Number
        self.widget_4 = QtWidgets.QWidget(parent=self.widget)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_4)

        self.id_number_text = QtWidgets.QLabel(parent=self.widget_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.id_number_text.setFont(font)
        self.horizontalLayout_3.addWidget(self.id_number_text)

        self.id_number_input = QtWidgets.QLineEdit(parent=self.widget_4)
        self.id_number_input.setMinimumSize(QtCore.QSize(101, 41))
        self.id_number_input.setMaximumSize(QtCore.QSize(101, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.id_number_input.setFont(font)
        self.id_number_input.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        regex = QtCore.QRegularExpression(r"^\d{4}-\d{4}$")
        validator = QtGui.QRegularExpressionValidator(regex)
        self.id_number_input.setValidator(validator)

        self.horizontalLayout_3.addWidget(self.id_number_input)

        spacerItem1 = QtWidgets.QSpacerItem(
            236, 20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum
        )
        self.horizontalLayout_3.addItem(spacerItem1)

        self.gridLayout.addWidget(self.widget_4, 2, 0, 1, 1)

        # First Name
        self.widget_5 = QtWidgets.QWidget(parent=self.widget)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_5)

        self.first_name_text = QtWidgets.QLabel(parent=self.widget_5)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.first_name_text.setFont(font)
        self.horizontalLayout_4.addWidget(self.first_name_text)

        self.first_name_input = QtWidgets.QLineEdit(parent=self.widget_5)
        self.first_name_input.setMinimumSize(QtCore.QSize(291, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.first_name_input.setFont(font)
        self.horizontalLayout_4.addWidget(self.first_name_input)

        self.gridLayout.addWidget(self.widget_5, 3, 0, 1, 1)

        # Last Name
        self.widget_6 = QtWidgets.QWidget(parent=self.widget)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget_6)

        self.last_name_text = QtWidgets.QLabel(parent=self.widget_6)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.last_name_text.setFont(font)
        self.horizontalLayout_5.addWidget(self.last_name_text)

        self.last_name_input = QtWidgets.QLineEdit(parent=self.widget_6)
        self.last_name_input.setMinimumSize(QtCore.QSize(171, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.last_name_input.setFont(font)
        self.horizontalLayout_5.addWidget(self.last_name_input)

        self.gridLayout.addWidget(self.widget_6, 4, 0, 1, 1)

        # Gender
        self.widget_8 = QtWidgets.QWidget(parent=self.widget)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.widget_8)

        self.gender_text = QtWidgets.QLabel(parent=self.widget_8)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.gender_text.setFont(font)
        self.horizontalLayout_7.addWidget(self.gender_text)

        self.gender_comboBox = QtWidgets.QComboBox(parent=self.widget_8)
        self.gender_comboBox.setMinimumSize(QtCore.QSize(91, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.gender_comboBox.setFont(font)
        self.gender_comboBox.addItems(["Male", "Female"])
        self.horizontalLayout_7.addWidget(self.gender_comboBox)

        spacerItem2 = QtWidgets.QSpacerItem(
            278, 20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum
        )
        self.horizontalLayout_7.addItem(spacerItem2)

        self.gridLayout.addWidget(self.widget_8, 5, 0, 1, 1)

        # Year Level
        self.widget_7 = QtWidgets.QWidget(parent=self.widget)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.widget_7)

        self.year_level_text = QtWidgets.QLabel(parent=self.widget_7)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.year_level_text.setFont(font)
        self.horizontalLayout_6.addWidget(self.year_level_text)

        self.year_level_comboBox = QtWidgets.QComboBox(parent=self.widget_7)
        self.year_level_comboBox.setMinimumSize(QtCore.QSize(61, 41))
        self.year_level_comboBox.setMaximumSize(QtCore.QSize(61, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.year_level_comboBox.setFont(font)
        self.year_level_comboBox.addItems(["1", "2", "3", "4"])
        self.horizontalLayout_6.addWidget(self.year_level_comboBox)

        spacerItem3 = QtWidgets.QSpacerItem(
            282, 20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum
        )
        self.horizontalLayout_6.addItem(spacerItem3)

        self.gridLayout.addWidget(self.widget_7, 6, 0, 1, 1)

        # Program Code
        self.widget_9 = QtWidgets.QWidget(parent=self.widget)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.widget_9)

        self.Program_Code_text = QtWidgets.QLabel(parent=self.widget_9)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.Program_Code_text.setFont(font)
        self.horizontalLayout_8.addWidget(self.Program_Code_text)

        self.program_code_input_comboBox = QtWidgets.QComboBox(parent=self.widget_9)
        self.program_code_input_comboBox.setMinimumSize(QtCore.QSize(101, 41))
        self.program_code_input_comboBox.setMaximumSize(QtCore.QSize(121, 41))
        self.horizontalLayout_8.addWidget(self.program_code_input_comboBox)

        spacerItem4 = QtWidgets.QSpacerItem(
            209, 20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum
        )
        self.horizontalLayout_8.addItem(spacerItem4)

        self.gridLayout.addWidget(self.widget_9, 7, 0, 1, 1)

        # Buttons
        self.widget_2 = QtWidgets.QWidget(parent=self.widget)
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_2)

        spacerItem5 = QtWidgets.QSpacerItem(
            76, 20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum
        )
        self.horizontalLayout.addItem(spacerItem5)

        self.Save_button = QtWidgets.QPushButton(parent=self.widget_2)
        self.Save_button.setMinimumSize(QtCore.QSize(93, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Save_button.setFont(font)
        self.horizontalLayout.addWidget(self.Save_button)

        spacerItem6 = QtWidgets.QSpacerItem(
            75, 20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum
        )
        self.horizontalLayout.addItem(spacerItem6)

        self.Cancel_button = QtWidgets.QPushButton(parent=self.widget_2)
        self.Cancel_button.setMinimumSize(QtCore.QSize(93, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Cancel_button.setFont(font)
        self.horizontalLayout.addWidget(self.Cancel_button)

        spacerItem7 = QtWidgets.QSpacerItem(
            40, 20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum
        )
        self.horizontalLayout.addItem(spacerItem7)

        self.gridLayout.addWidget(self.widget_2, 8, 0, 1, 1)

        self.gridLayout_2.addWidget(self.widget, 0, 0, 1, 1)

        self.retranslateUi(AddStudent_Dialog)
        QtCore.QMetaObject.connectSlotsByName(AddStudent_Dialog)

    def retranslateUi(self, AddStudent_Dialog):
        _translate = QtCore.QCoreApplication.translate
        AddStudent_Dialog.setWindowTitle(_translate("AddStudent_Dialog", "Dialog"))
        self.Edit_Student_text.setText(_translate("AddStudent_Dialog", "Add Student Information"))
        self.id_number_text.setText(_translate("AddStudent_Dialog", "ID Number"))
        self.id_number_input.setPlaceholderText(_translate("AddStudent_Dialog", "2025-0001"))
        self.first_name_text.setText(_translate("AddStudent_Dialog", "First Name"))
        self.last_name_text.setText(_translate("AddStudent_Dialog", "Last Name"))
        self.gender_text.setText(_translate("AddStudent_Dialog", "Gender"))
        self.year_level_text.setText(_translate("AddStudent_Dialog", "Year Level"))
        self.Program_Code_text.setText(_translate("AddStudent_Dialog", "Program Code"))
        self.Save_button.setText(_translate("AddStudent_Dialog", "Save"))
        self.Cancel_button.setText(_translate("AddStudent_Dialog", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AddStudent_Dialog = QtWidgets.QDialog()
    ui = add_Student()
    ui.setupUi(AddStudent_Dialog)
    AddStudent_Dialog.show()
    sys.exit(app.exec())
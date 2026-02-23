from PyQt6 import QtCore, QtGui, QtWidgets


class update_Student(object):
    def setupUi(self, EditStudent_Dialog):
        EditStudent_Dialog.setObjectName("EditStudent_Dialog")
        EditStudent_Dialog.resize(500, 532)
        EditStudent_Dialog.setMinimumSize(QtCore.QSize(500, 532))

        self.gridLayout_2 = QtWidgets.QGridLayout(EditStudent_Dialog)

        self.widget = QtWidgets.QWidget(parent=EditStudent_Dialog)
        self.widget.setMinimumSize(QtCore.QSize(481, 513))
        self.gridLayout = QtWidgets.QGridLayout(self.widget)

        # ===== Title =====
        self.widget_3 = QtWidgets.QWidget(parent=self.widget)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_3)

        self.Edit_Student_text = QtWidgets.QLabel(parent=self.widget_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.Edit_Student_text.setFont(font)

        self.horizontalLayout_2.addWidget(self.Edit_Student_text)
        self.horizontalLayout_2.addItem(
            QtWidgets.QSpacerItem(40, 20,
                                  QtWidgets.QSizePolicy.Policy.Expanding,
                                  QtWidgets.QSizePolicy.Policy.Minimum)
        )

        self.gridLayout.addWidget(self.widget_3, 0, 0, 1, 1)

        # ===== Line =====
        self.line = QtWidgets.QFrame(parent=self.widget)
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.gridLayout.addWidget(self.line, 1, 0, 1, 1)

        # ===== ID Number =====
        self.widget_4 = QtWidgets.QWidget(parent=self.widget)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_4)

        self.id_number_text = QtWidgets.QLabel(parent=self.widget_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.id_number_text.setFont(font)

        self.id_number_input = QtWidgets.QLineEdit(parent=self.widget_4)
        self.id_number_input.setMinimumSize(QtCore.QSize(101, 41))
        self.id_number_input.setMaximumSize(QtCore.QSize(101, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.id_number_input.setFont(font)
        self.id_number_input.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.id_number_text)
        self.horizontalLayout_3.addWidget(self.id_number_input)
        self.horizontalLayout_3.addItem(
            QtWidgets.QSpacerItem(236, 20,
                                  QtWidgets.QSizePolicy.Policy.Expanding,
                                  QtWidgets.QSizePolicy.Policy.Minimum)
        )

        self.gridLayout.addWidget(self.widget_4, 2, 0, 1, 1)

        # ===== First Name =====
        self.widget_5 = QtWidgets.QWidget(parent=self.widget)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_5)

        self.first_name_text = QtWidgets.QLabel(parent=self.widget_5)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.first_name_text.setFont(font)

        self.first_name_input = QtWidgets.QLineEdit(parent=self.widget_5)
        self.first_name_input.setMinimumSize(QtCore.QSize(291, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.first_name_input.setFont(font)

        self.horizontalLayout_4.addWidget(self.first_name_text)
        self.horizontalLayout_4.addWidget(self.first_name_input)

        self.gridLayout.addWidget(self.widget_5, 3, 0, 1, 1)

        # ===== Last Name =====
        self.widget_6 = QtWidgets.QWidget(parent=self.widget)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget_6)

        self.last_name_text = QtWidgets.QLabel(parent=self.widget_6)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.last_name_text.setFont(font)

        self.last_name_input = QtWidgets.QLineEdit(parent=self.widget_6)
        self.last_name_input.setMinimumSize(QtCore.QSize(171, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.last_name_input.setFont(font)

        self.horizontalLayout_5.addWidget(self.last_name_text)
        self.horizontalLayout_5.addWidget(self.last_name_input)

        self.gridLayout.addWidget(self.widget_6, 4, 0, 1, 1)

        # ===== Gender =====
        self.widget_8 = QtWidgets.QWidget(parent=self.widget)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.widget_8)

        self.Gender_text = QtWidgets.QLabel(parent=self.widget_8)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.Gender_text.setFont(font)

        self.gender_comboBox = QtWidgets.QComboBox(parent=self.widget_8)
        self.gender_comboBox.setMinimumSize(QtCore.QSize(91, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.gender_comboBox.setFont(font)

        self.horizontalLayout_7.addWidget(self.Gender_text)
        self.horizontalLayout_7.addWidget(self.gender_comboBox)
        self.horizontalLayout_7.addItem(
            QtWidgets.QSpacerItem(278, 20,
                                  QtWidgets.QSizePolicy.Policy.Expanding,
                                  QtWidgets.QSizePolicy.Policy.Minimum)
        )

        self.gridLayout.addWidget(self.widget_8, 5, 0, 1, 1)

        # ===== Year Level =====
        self.widget_7 = QtWidgets.QWidget(parent=self.widget)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.widget_7)

        self.year_level_text = QtWidgets.QLabel(parent=self.widget_7)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.year_level_text.setFont(font)

        self.year_level_comboBox = QtWidgets.QComboBox(parent=self.widget_7)
        self.year_level_comboBox.setMinimumSize(QtCore.QSize(61, 41))
        self.year_level_comboBox.setMaximumSize(QtCore.QSize(61, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.year_level_comboBox.setFont(font)

        self.horizontalLayout_6.addWidget(self.year_level_text)
        self.horizontalLayout_6.addWidget(self.year_level_comboBox)
        self.horizontalLayout_6.addItem(
            QtWidgets.QSpacerItem(282, 20,
                                  QtWidgets.QSizePolicy.Policy.Expanding,
                                  QtWidgets.QSizePolicy.Policy.Minimum)
        )

        self.gridLayout.addWidget(self.widget_7, 6, 0, 1, 1)

        # ===== Program Code =====
        self.widget_9 = QtWidgets.QWidget(parent=self.widget)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.widget_9)

        self.program_code_text = QtWidgets.QLabel(parent=self.widget_9)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.program_code_text.setFont(font)

        self.program_code_input_comboBox = QtWidgets.QComboBox(parent=self.widget_9)
        self.program_code_input_comboBox.setMinimumSize(QtCore.QSize(101, 41))
        self.program_code_input_comboBox.setMaximumSize(QtCore.QSize(121, 41))

        self.horizontalLayout_8.addWidget(self.program_code_text)
        self.horizontalLayout_8.addWidget(self.program_code_input_comboBox)
        self.horizontalLayout_8.addItem(
            QtWidgets.QSpacerItem(209, 20,
                                  QtWidgets.QSizePolicy.Policy.Expanding,
                                  QtWidgets.QSizePolicy.Policy.Minimum)
        )

        self.gridLayout.addWidget(self.widget_9, 7, 0, 1, 1)

        # ===== Buttons =====
        self.widget_2 = QtWidgets.QWidget(parent=self.widget)
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_2)

        self.horizontalLayout.addItem(
            QtWidgets.QSpacerItem(76, 20,
                                  QtWidgets.QSizePolicy.Policy.Expanding,
                                  QtWidgets.QSizePolicy.Policy.Minimum)
        )

        self.Save_button = QtWidgets.QPushButton(parent=self.widget_2)
        self.Save_button.setMinimumSize(QtCore.QSize(93, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Save_button.setFont(font)

        self.horizontalLayout.addWidget(self.Save_button)

        self.horizontalLayout.addItem(
            QtWidgets.QSpacerItem(75, 20,
                                  QtWidgets.QSizePolicy.Policy.Expanding,
                                  QtWidgets.QSizePolicy.Policy.Minimum)
        )

        self.Cancel_button = QtWidgets.QPushButton(parent=self.widget_2)
        self.Cancel_button.setMinimumSize(QtCore.QSize(93, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Cancel_button.setFont(font)

        self.horizontalLayout.addWidget(self.Cancel_button)

        self.horizontalLayout.addItem(
            QtWidgets.QSpacerItem(40, 20,
                                  QtWidgets.QSizePolicy.Policy.Expanding,
                                  QtWidgets.QSizePolicy.Policy.Minimum)
        )

        self.gridLayout.addWidget(self.widget_2, 8, 0, 1, 1)
        self.gridLayout_2.addWidget(self.widget, 0, 0, 1, 1)

        self.retranslateUi(EditStudent_Dialog)
        QtCore.QMetaObject.connectSlotsByName(EditStudent_Dialog)

    def retranslateUi(self, EditStudent_Dialog):
        _translate = QtCore.QCoreApplication.translate
        EditStudent_Dialog.setWindowTitle(_translate("EditStudent_Dialog", "Dialog"))
        self.Edit_Student_text.setText(_translate("EditStudent_Dialog", "Update Student Information"))
        self.id_number_text.setText(_translate("EditStudent_Dialog", "ID Number"))
        self.id_number_input.setPlaceholderText(_translate("EditStudent_Dialog", "YYYY-NNNN"))
        self.first_name_text.setText(_translate("EditStudent_Dialog", "First Name"))
        self.last_name_text.setText(_translate("EditStudent_Dialog", "Last Name"))
        self.Gender_text.setText(_translate("EditStudent_Dialog", "Gender"))
        self.gender_comboBox.addItems(["Male", "Female"])
        self.year_level_text.setText(_translate("EditStudent_Dialog", "Year Level"))
        self.year_level_comboBox.addItems(["1", "2", "3", "4"])
        self.program_code_text.setText(_translate("EditStudent_Dialog", "Program Code"))
        self.Save_button.setText(_translate("EditStudent_Dialog", "Save"))
        self.Cancel_button.setText(_translate("EditStudent_Dialog", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    EditStudent_Dialog = QtWidgets.QDialog()
    ui = update_Student()
    ui.setupUi(EditStudent_Dialog)
    EditStudent_Dialog.show()
    sys.exit(app.exec())
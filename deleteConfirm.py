from PyQt6 import QtCore, QtGui, QtWidgets


class deleteConfirm(object):
    def setupUi(self, DeleteConfirmation):
        DeleteConfirmation.setObjectName("DeleteConfirmation")
        DeleteConfirmation.resize(387, 178)
        DeleteConfirmation.setMinimumSize(QtCore.QSize(387, 178))
        DeleteConfirmation.setMaximumSize(QtCore.QSize(387, 178))

        # Label
        self.Text = QtWidgets.QLabel(parent=DeleteConfirmation)
        self.Text.setGeometry(QtCore.QRect(10, 40, 362, 22))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Text.setFont(font)
        self.Text.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        # Buttons Widget
        self.widget = QtWidgets.QWidget(parent=DeleteConfirmation)
        self.widget.setGeometry(QtCore.QRect(11, 120, 361, 35))
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)

        # Spacer
        spacerItem = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum
        )
        self.horizontalLayout.addItem(spacerItem)

        # Cancel Button
        self.Cancel = QtWidgets.QPushButton(parent=self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Cancel.setFont(font)
        self.horizontalLayout.addWidget(self.Cancel)

        # Confirm Button
        self.Confirm = QtWidgets.QPushButton(parent=self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Confirm.setFont(font)
        self.horizontalLayout.addWidget(self.Confirm)

        self.retranslateUi(DeleteConfirmation)
        QtCore.QMetaObject.connectSlotsByName(DeleteConfirmation)

    def retranslateUi(self, DeleteConfirmation):
        _translate = QtCore.QCoreApplication.translate
        DeleteConfirmation.setWindowTitle(_translate("DeleteConfirmation", "Dialog"))
        self.Text.setText(
            _translate("DeleteConfirmation", "Are you sure you want to delete this item?")
        )
        self.Cancel.setText(_translate("DeleteConfirmation", "Cancel"))
        self.Confirm.setText(_translate("DeleteConfirmation", "Confirm"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dialog = QtWidgets.QDialog()
    ui = deleteConfirm()
    ui.setupUi(dialog)
    dialog.show()
    sys.exit(app.exec())
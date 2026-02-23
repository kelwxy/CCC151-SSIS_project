import sys
import os
import csv

from model import config_file

from model.existence_checker import programName_existence, programCode_existence, collegeCode_existence, collegeName_existence, idNumber_existence

from PyQt6.QtWidgets import QMainWindow, QApplication, QDialog, QTableWidgetItem, QPushButton, QWidget, QHBoxLayout, QMessageBox
from PyQt6 import QtWidgets, QtCore

from _addFolder.addCollege import add_College
from _addFolder.addProgram import add_Program
from _addFolder.addStudent import add_Student

from _updateFolder.updateCollege import update_College
from _updateFolder.updateProgram import update_Program
from _updateFolder.updateStudent import update_Student

from _loginFolder.loginDialog import login_Dialog

from deleteConfirm import delete_Confirm
from mainWindow import main_Window


CREDENTIALS = {
    "Admin": {"username": "admin", "password": "admin123"},
    "User":  {"username": "user",  "password": "user123"},
}


class Login_Dialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = login_Dialog()
        self.ui.setupUi(self)
        self.role = None
        self.ui.login_button.clicked.connect(self.handle_login)

    def handle_login(self):
        username = self.ui.username_input.text().strip()
        password = self.ui.password_input.text().strip()
        role = self.ui.role_comboBox.currentText()  # "Admin" or "User"

        creds = CREDENTIALS.get(role)
        if creds and username == creds["username"] and password == creds["password"]:
            self.role = role
            self.accept()
        else:
            self.ui.error_label.setText("Invalid username or password.")


def create_csv_file(filename, fieldnames):
    if not os.path.isfile(filename):
        with open(filename, "w", newline="") as f:
            csv.DictWriter(f, fieldnames=fieldnames).writeheader()
            print(f" Created: {filename}")


def read_csv(filename):
    with open(filename, "r", newline="") as f:
        return list(csv.reader(f))


def write_csv(filename, data):
    with open(filename, "w", newline="") as f:
        csv.writer(f).writerows(data)


def load_combobox(combobox, filename, field):
    if not os.path.isfile(filename):
        return
    with open(filename, "r", newline="") as f:
        for row in csv.DictReader(f):
            if value := row.get(field):
                combobox.addItem(value)


def update_csv_field(filename, col_index, old_value, new_value):
    data = read_csv(filename)
    if not data:
        return
    header, rows = data[0], data[1:]
    for row in rows:
        if len(row) > col_index and row[col_index].strip() == old_value:
            row[col_index] = new_value
    write_csv(filename, [header] + rows)


for fname, fnames in [
    (config_file.student_filename, config_file.student_fieldnames),
    (config_file.program_filename, config_file.program_fieldnames),
    (config_file.college_filename, config_file.college_fieldnames),
]:
    create_csv_file(fname, fnames)


class Add_College_Dialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = add_College()
        self.ui.setupUi(self)
        self.ui.Save_button.clicked.connect(self.save_college)
        self.ui.Cancel_button.clicked.connect(self.reject)

    def save_college(self):
        code = self.ui.CollegeCode_input.text()
        name = self.ui.CollegeName_input.text()

        if not code or not name:
            return QMessageBox.warning(self, "Error", "All field must be filled out")
        if collegeCode_existence(config_file.college_filename, code):
            return QMessageBox.warning(self, "Error", "College code already exists, please change it")
        if collegeName_existence(config_file.college_filename, name):
            return QMessageBox.warning(self, "Error", "College name already exists, please change it")

        file_exists = os.path.isfile(config_file.college_filename)
        with open(config_file.college_filename, "a", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=config_file.college_fieldnames)
            if not file_exists:
                writer.writeheader()
            writer.writerow({"college_code": code, "college_name": name})

        self.parent().load_csv_to_table(self.parent().college_table, config_file.college_filename, "COLLEGES")
        self.parent().sort_table()
        self.accept()


class Add_Program_Dialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = add_Program()
        self.ui.setupUi(self)
        load_combobox(self.ui.college_code_input_comboBox, config_file.college_filename, "college_code")
        self.ui.Save_button.clicked.connect(self.save_program)
        self.ui.Cancel_button.clicked.connect(self.reject)

    def save_program(self):
        code = self.ui.ProgramCode_input.text()
        name = self.ui.ProgramName_input.text()
        college = self.ui.college_code_input_comboBox.currentText()

        if not code or not name or not college:
            return QMessageBox.warning(self, "Error", "All fields must be filled")
        if programName_existence(config_file.program_filename, name):
            return QMessageBox.warning(self, "Error", "Program Name already exists!")
        if programCode_existence(config_file.program_filename, code):
            return QMessageBox.warning(self, "Error", "Program Code already exists!")

        file_exists = os.path.isfile(config_file.program_filename)
        with open(config_file.program_filename, "a", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=config_file.program_fieldnames)
            if not file_exists:
                writer.writeheader()
            writer.writerow({"program_code": code, "program_name": name, "college_code": college})

        self.parent().load_csv_to_table(self.parent().program_table, config_file.program_filename, "PROGRAMS")
        self.parent().sort_table()
        self.accept()


class Add_Student_Dialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = add_Student()
        self.ui.setupUi(self)
        load_combobox(self.ui.program_code_input_comboBox, config_file.program_filename, "program_code")
        self.ui.Save_button.clicked.connect(self.save_student)
        self.ui.Cancel_button.clicked.connect(self.reject)

    def save_student(self):
        id_number = self.ui.id_number_input.text()
        first_name = self.ui.first_name_input.text()
        last_name = self.ui.last_name_input.text()
        gender = self.ui.gender_comboBox.currentText()
        year_level = self.ui.year_level_comboBox.currentText()
        program_code = self.ui.program_code_input_comboBox.currentText()

        if not all([id_number, first_name, last_name, year_level, gender, program_code]):
            return QMessageBox.warning(self, "Input Error", "All fields must be filled out.")
        if idNumber_existence(config_file.student_filename, id_number):
            return QMessageBox.warning(self, "Error", "ID Number already exists")
        if not programCode_existence(config_file.program_filename, program_code):
            return QMessageBox.warning(self, "Error", "Program Code doesn't exists! Enter a valid program code")

        file_exists = os.path.isfile(config_file.student_filename)
        with open(config_file.student_filename, "a", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=config_file.student_fieldnames)
            if not file_exists:
                writer.writeheader()
            writer.writerow({
                "id_number": id_number, "first_name": first_name, "last_name": last_name,
                "gender": gender, "year_level": year_level, "program_code": program_code
            })

        self.parent().load_csv_to_table(self.parent().student_table, config_file.student_filename, "STUDENTS")
        self.parent().sort_table()
        self.accept()


class Edit_College_Dialog(QDialog):
    def __init__(self, parent, row_data, row_index):
        super().__init__(parent)
        self.ui = update_College()
        self.ui.setupUi(self)
        self.row_index = row_index
        self.parent = parent
        self.old_college_code, self.old_college_name = row_data[0], row_data[1]
        self.ui.college_code_input.setText(row_data[0])
        self.ui.college_name_input.setText(row_data[1])
        self.ui.Save_button.clicked.connect(self.save_changes)
        self.ui.Cancel_button.clicked.connect(self.reject)

    def save_changes(self):
        new_code = self.ui.college_code_input.text().strip()
        new_name = self.ui.college_name_input.text().strip()

        if not new_code or not new_name:
            return QMessageBox.warning(self, "Error", "Fields cannot be empty!")
        if new_code != self.old_college_code and collegeCode_existence(config_file.college_filename, new_code):
            return QMessageBox.warning(self, "Error", "College code already exists!")
        if new_name != self.old_college_name and collegeName_existence(config_file.college_filename, new_name):
            return QMessageBox.warning(self, "Error", "College already exists!")

        data = read_csv(config_file.college_filename)
        if 1 <= self.row_index < len(data):
            data[self.row_index] = [new_code, new_name]
        write_csv(config_file.college_filename, data)

        if new_code != self.old_college_code:
            update_csv_field(config_file.program_filename, 2, self.old_college_code, new_code)

        self.parent.load_csv_to_table(self.parent.program_table, config_file.program_filename, "PROGRAMS")
        self.parent.load_csv_to_table(self.parent.college_table, config_file.college_filename, "COLLEGES")
        self.accept()


class Edit_Program_Dialog(QDialog):
    def __init__(self, parent, row_data, row_index):
        super().__init__(parent)
        self.ui = update_Program()
        self.ui.setupUi(self)
        self.row_index = row_index
        self.parent = parent
        self.old_program_code, self.old_program_name, self.old_college_code = row_data[0], row_data[1], row_data[2]
        load_combobox(self.ui.college_code_input_comboBox, config_file.college_filename, "college_code")
        self.ui.program_code_input.setText(row_data[0])
        self.ui.program_name_input.setText(row_data[1])
        self.ui.college_code_input_comboBox.setCurrentText(row_data[2])
        self.ui.Save_button.clicked.connect(self.save_changes)
        self.ui.Cancel_button.clicked.connect(self.reject)

    def save_changes(self):
        new_code = self.ui.program_code_input.text().strip()
        new_name = self.ui.program_name_input.text().strip()
        new_college = self.ui.college_code_input_comboBox.currentText()

        if not new_code or not new_name or not new_college:
            return QMessageBox.warning(self, "Error", "All fields must not be empty!")
        if new_code != self.old_program_code and programCode_existence(config_file.program_filename, new_code):
            return QMessageBox.warning(self, "Error", "Program code already exists")
        if new_name != self.old_program_name and programName_existence(config_file.program_filename, new_name):
            return QMessageBox.warning(self, "Error", "Program name already exists!")

        data = read_csv(config_file.program_filename)
        if 1 <= self.row_index < len(data):
            data[self.row_index] = [new_code, new_name, new_college]
        write_csv(config_file.program_filename, data)

        if new_code != self.old_program_code:
            update_csv_field(config_file.student_filename, 5, self.old_program_code, new_code)

        self.parent.load_csv_to_table(self.parent.student_table, config_file.student_filename, "STUDENTS")
        self.parent.load_csv_to_table(self.parent.program_table, config_file.program_filename, "PROGRAMS")
        self.accept()


class Edit_Student_Dialog(QDialog):
    def __init__(self, parent, row_data, row_index):
        super().__init__(parent)
        self.ui = update_Student()
        self.ui.setupUi(self)
        self.row_index = row_index
        self.parent = parent
        self.old_id_number = row_data[0]
        load_combobox(self.ui.program_code_input_comboBox, config_file.program_filename, "program_code")
        self.ui.id_number_input.setText(row_data[0])
        self.ui.first_name_input.setText(row_data[1])
        self.ui.last_name_input.setText(row_data[2])
        self.ui.gender_comboBox.setCurrentText(row_data[3])
        self.ui.year_level_comboBox.setCurrentText(row_data[4])
        self.ui.program_code_input_comboBox.setCurrentText(row_data[5])
        self.ui.Save_button.clicked.connect(self.save_changes)
        self.ui.Cancel_button.clicked.connect(self.reject)

    def save_changes(self):
        new_id = self.ui.id_number_input.text().strip()
        new_first = self.ui.first_name_input.text().strip()
        new_last = self.ui.last_name_input.text().strip()
        new_gender = self.ui.gender_comboBox.currentText()
        new_year = self.ui.year_level_comboBox.currentText()
        new_program = self.ui.program_code_input_comboBox.currentText()

        if not all([new_id, new_first, new_last, new_gender, new_year, new_program]):
            return QMessageBox.warning(self, "Error", "All fields must not be empty!")
        if new_id != self.old_id_number and idNumber_existence(config_file.student_filename, new_id):
            return QMessageBox.warning(self, "Error", "ID Number already exists!")

        data = read_csv(config_file.student_filename)
        if 1 <= self.row_index < len(data):
            data[self.row_index] = [new_id, new_first, new_last, new_gender, new_year, new_program]
        write_csv(config_file.student_filename, data)

        self.parent.load_csv_to_table(self.parent.student_table, config_file.student_filename, "STUDENTS")
        self.accept()


class DeleteItemConfirmation(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = delete_Confirm()
        self.ui.setupUi(self)
        self.ui.Confirm.clicked.connect(self.accept)
        self.ui.Cancel.clicked.connect(self.reject)


class MainWindow(QMainWindow):
    def __init__(self, role):
        super(MainWindow, self).__init__()
        self.role = role
        self.is_admin = role == "Admin"
        self.ui = main_Window()
        self.ui.setupUi(self)

        self.ui.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.ui.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.NoSelection)
        self.ui.search_text.textChanged.connect(self.search_table)

        self.student_table = self.ui.tableWidget
        self.program_table = self.ui.tableWidget_2
        self.college_table = self.ui.tableWidget_3

        for table in [self.student_table, self.program_table, self.college_table]:
            table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)

        self.ui.exit_button.clicked.connect(QApplication.instance().quit)
        self.ui.students_button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))
        self.ui.programs_button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(1))
        self.ui.colleges_button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(2))
        self.ui.stackedWidget.currentChanged.connect(self.on_page_changed)

        if self.is_admin:
            self.ui.addstudent_button.clicked.connect(self.open_add_student_dialog)
            self.ui.addprogram_button.clicked.connect(self.open_add_program_dialog)
            self.ui.addcollege_button.clicked.connect(self.open_add_college_dialog)
        else:
            self.ui.addstudent_button.setVisible(False)
            self.ui.addprogram_button.setVisible(False)
            self.ui.addcollege_button.setVisible(False)

        self.load_csv_to_table(self.student_table, config_file.student_filename, "STUDENTS")
        self.load_csv_to_table(self.program_table, config_file.program_filename, "PROGRAMS")
        self.load_csv_to_table(self.college_table, config_file.college_filename, "COLLEGES")

        self.ui.comboBox.currentIndexChanged.connect(self.sort_table)
        self.ui.comboBox_2.currentIndexChanged.connect(self.sort_table)
        self.ui.comboBox_3.currentIndexChanged.connect(self.sort_table)

    def open_add_student_dialog(self):
        Add_Student_Dialog(self).exec()

    def open_add_program_dialog(self):
        Add_Program_Dialog(self).exec()

    def open_add_college_dialog(self):
        Add_College_Dialog(self).exec()

    def load_csv_to_table(self, table_widget, filename, table_type):
        if not os.path.isfile(filename):
            return print(f" File {filename} does not exist yet.")

        data = read_csv(filename)
        if not data:
            return print(f" {filename} is empty.")

        readable_headers = [h[1] for h in config_file.header_names.get(table_type, [])]
        table_widget.setHorizontalHeaderLabels(readable_headers + ["Actions"])

        rows = data[1:]
        table_widget.setRowCount(len(rows))
        for row_index, row in enumerate(rows):
            for col_index, value in enumerate(row):
                if col_index < table_widget.columnCount() - 1:
                    table_widget.setItem(row_index, col_index, QTableWidgetItem(value))

            action_widget = QWidget()
            layout = QHBoxLayout(action_widget)
            layout.setContentsMargins(0, 0, 0, 0)

            if self.is_admin:
                edit_btn = QPushButton("Edit")
                edit_btn.clicked.connect(lambda _, ri=row_index: self.edit_row(table_widget, filename, ri))
                layout.addWidget(edit_btn)

                del_btn = QPushButton("Delete")
                del_btn.clicked.connect(lambda _, ri=row_index: self.confirm_delete_Row(table_widget, filename, ri))
                layout.addWidget(del_btn)
            else:
                view_label = QtWidgets.QLabel("View Only")
                view_label.setStyleSheet("color: gray; font-style: italic;")
                layout.addWidget(view_label)

            table_widget.setCellWidget(row_index, len(readable_headers), action_widget)

        print(f" Loaded {filename} into {table_type} table with custom headers.")

    def edit_row(self, table_widget, filename, row_index):
        print(f"Editing row {row_index} in {filename}")
        data = read_csv(filename)
        row_index += 1

        if row_index < 1 or row_index >= len(data):
            return print("Invalid row index. Skipping edit.")

        dialog_map = {
            config_file.student_filename: (Edit_Student_Dialog, "STUDENTS"),
            config_file.program_filename: (Edit_Program_Dialog, "PROGRAMS"),
            config_file.college_filename: (Edit_College_Dialog, "COLLEGES"),
        }

        if filename not in dialog_map:
            return print("⚠️ Unknown CSV file. Skipping edit.")

        DialogClass, table_type = dialog_map[filename]
        if DialogClass(self, data[row_index], row_index).exec():
            self.load_csv_to_table(table_widget, filename, table_type)

    def delete_row(self, table_widget, filename, row_index):
        print(f"Deleting row {row_index} from {filename}")
        data = read_csv(filename)
        row_index += 1

        if row_index < 1 or row_index >= len(data):
            return print("Invalid row index. Skipping deletion.")

        deleted_row = data.pop(row_index)
        write_csv(filename, data)
        table_widget.removeRow(row_index)
        print("Row deleted successfully and CSV updated.")

        if filename == config_file.college_filename:
            self.update_programs_after_college_delete(deleted_row[0])
        elif filename == config_file.program_filename:
            self.update_students_after_program_delete(deleted_row[0])

        table_type_map = {
            config_file.student_filename: "STUDENTS",
            config_file.program_filename: "PROGRAMS",
            config_file.college_filename: "COLLEGES",
        }
        if filename not in table_type_map:
            return print("⚠️ Unknown CSV file. Skipping refresh.")

        self.load_csv_to_table(table_widget, filename, table_type_map[filename])

    def confirm_delete_Row(self, table_widget, filename, row_index):
        if DeleteItemConfirmation().exec() == QDialog.DialogCode.Accepted:
            self.delete_row(table_widget, filename, row_index)
        else:
            print("Cancelled")

    def on_page_changed(self, index):
        self.ui.SearchFilters.setCurrentIndex({0: 1, 1: 4, 2: 6}.get(index, 0))

    def search_table(self):
        search_text = self.ui.search_text.text().strip().lower()
        current_index = self.ui.stackedWidget.currentIndex()
        table_map = {0: (self.student_table, 1), 1: (self.program_table, 4), 2: (self.college_table, 6)}

        if current_index not in table_map:
            return print("⚠️ No valid table selected!")

        table_widget, offset = table_map[current_index]
        col = self.ui.SearchFilters.currentIndex() - offset

        for row in range(table_widget.rowCount()):
            item = table_widget.item(row, col)
            hide = bool(search_text) and not (item and search_text in item.text().strip().lower())
            table_widget.setRowHidden(row, hide)

    def sort_table(self):
        current_index = self.ui.stackedWidget.currentIndex()
        ASC, DESC = QtCore.Qt.SortOrder.AscendingOrder, QtCore.Qt.SortOrder.DescendingOrder

        config_map = {
            0: (self.student_table, config_file.student_filename, "STUDENTS", self.ui.comboBox, {
                1: (1, ASC), 2: (1, DESC), 3: (2, ASC), 4: (2, DESC),
                5: (0, ASC), 6: (0, DESC), 7: (3, ASC), 8: (3, DESC),
                9: (5, ASC), 10: (4, ASC)
            }),
            1: (self.program_table, config_file.program_filename, "PROGRAMS", self.ui.comboBox_2, {
                1: (0, ASC), 2: (0, DESC), 3: (1, ASC), 4: (1, DESC), 5: (2, ASC), 6: (2, DESC)
            }),
            2: (self.college_table, config_file.college_filename, "COLLEGES", self.ui.comboBox_3, {
                1: (0, ASC), 2: (0, DESC), 3: (1, ASC), 4: (1, DESC)
            }),
        }

        if current_index not in config_map:
            return print("⚠️ No active table found.")

        table_widget, filename, table_type, sort_combo, sort_mapping = config_map[current_index]
        selected = sort_combo.currentIndex()

        if selected not in sort_mapping:
            return self.load_csv_to_table(table_widget, filename, table_type)

        col, order = sort_mapping[selected]
        table_widget.sortItems(col, order)

    def update_programs_after_college_delete(self, deleted_college_code):
        data = read_csv(config_file.program_filename)
        if not data:
            return
        header, rows = data[0], data[1:]
        for row in rows:
            if row[2] == deleted_college_code:
                row[2] = "N/A"
        write_csv(config_file.program_filename, [header] + rows)
        self.load_csv_to_table(self.program_table, config_file.program_filename, "PROGRAMS")
        self.update_students_after_program_delete("N/A")

    def update_students_after_program_delete(self, deleted_program_code):
        data = read_csv(config_file.student_filename)
        if not data:
            return
        header, rows = data[0], data[1:]
        for row in rows:
            if row[5] == deleted_program_code:
                row[5] = "Unenrolled"
        write_csv(config_file.student_filename, [header] + rows)
        self.load_csv_to_table(self.student_table, config_file.student_filename, "STUDENTS")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    login = Login_Dialog()
    if login.exec() == QDialog.DialogCode.Accepted:
        window = MainWindow(role=login.role)
        window.show()
        sys.exit(app.exec())
    else:
        sys.exit(0)
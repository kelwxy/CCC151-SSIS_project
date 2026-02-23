import csv
import config_file
from existence_checker import programCode_existence

def addStudent(id_number, first_name, last_name, year_level, gender, program_code):
    if not isinstance(id_number, str):
        raise Exception("ID Number is invalid!")
    if not isinstance(first_name, str):
        raise Exception("First Name is invalid")
    if not isinstance(last_name, str):
        raise Exception("Last Name is invalid")
    if not isinstance(year_level, int):
        raise Exception("Year level is invalid!")
    if not isinstance(gender, str) or not gender.isalpha():
        raise Exception("Gender is invalid")
    if not isinstance(program_code, str) or not program_code.isalpha():
        raise Exception("Program Code is invalid")
    if not programCode_existence(config_file.program_filename, program_code):
        raise Exception("Program doesn't exist")

    with open(config_file.student_filename, "a", newline="") as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=config_file.student_fieldnames)

        csv_writer.writerow ({
            "id_number" : id_number,
            "first_name" : first_name,
            "last_name" : last_name,
            "year_level" : year_level,
            "gender" : gender,
            "program_code" : program_code
        })
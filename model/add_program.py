import csv
import config_file
from existence_checker import collegeCode_existence

def addProgram(program_code, program_name, college_code):
    if not isinstance(program_code, str):
        raise Exception("Its not a valid program")
    if not isinstance(program_name,str):
        raise Exception("Its not a valid program name")
    if not isinstance(college_code, str):
        raise Exception("Not a valid college code")
    
    if not collegeCode_existence(config_file.college_filename, college_code):
        raise Exception("College doesn't exist")
    
    with open(config_file.program_filename, "a", newline="") as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=config_file.program_fieldnames)

        csv_writer.writerow ({
            "program_code": program_code,
            "program_name": program_name,
            "college_code": college_code,
        })
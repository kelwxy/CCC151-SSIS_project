import csv

def programName_existence(filename, program_name):
    with open(filename, newline="") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        prog_exists = any(row["program_name"].lower() == program_name.lower() for row in csv_reader)

        return prog_exists
    
def programCode_existence(filename, program_code):
    with open(filename, newline="") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        progcode_exists = any(row["program_code"].lower() == program_code.lower() for row in csv_reader)

        return progcode_exists
    
def collegeName_existence(filename, college_name):
    with open(filename, newline="") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        college_exists = any(row["college_name"].lower() == college_name.lower() for row in csv_reader)

        return college_exists
    
def collegeCode_existence(filename, college_code):
    with open(filename, newline="") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        collegecode_exists = any(row["college_code"].lower() == college_code.lower() for row in csv_reader)

        return collegecode_exists
    
def idNumber_existence(filename, id_number):
    with open(filename, newline="") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        idNumber_exists = any(row["id_number"].lower() == id_number.lower() for row in csv_reader)
        return idNumber_exists
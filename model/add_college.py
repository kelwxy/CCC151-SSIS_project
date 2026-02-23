import csv
import config_file

def addCollege(college_code, college_name):
    if not isinstance(college_code, str):
        raise Exception("College Code is invalid")
    if not isinstance(college_name, str):
        raise Exception("College name must be string")

    with open(config_file.college_filename, "a", newline="") as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=config_file.college_fieldnames)

        csv_writer.writerow ({
            "college_code" : college_code,
            "college_name" : college_name
        })
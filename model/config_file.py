student_filename = "studentInfo.csv"
program_filename = "studentProgram.csv"
college_filename = "studentCollege.csv"

student_fieldnames = ["id_number", "first_name", "last_name", "gender", "year_level",  "program_code"]
program_fieldnames = ["program_code", "program_name", "college_code"]
college_fieldnames = ["college_code", "college_name"]

header_names = {
    "STUDENTS": [
        ("id_number", "ID Number"),
        ("first_name", "First Name"),
        ("last_name", "Last Name"),
        ("gender", "Gender"),
        ("year_level", "Year Level"),
        ("program_code", "Program Code"),
    ],
    "PROGRAMS": [
        ("program_code", "Program Code"),
        ("program_name", "Program Name"),
        ("college_code", "College Code"),
    ],
    "COLLEGES": [
        ("college_code", "College Code"),
        ("college_name", "College Name"),
    ],
}

search_filter = {
    "student_search_filter": ["ID Number", "First Name", "Last Name", "Gender", "Year Level", "Program Code"],
    "program_search_filter": ["Program Code", "Program Name", "College Code"],
    "college_search_filter": ["College Code", "College Name"] 
}
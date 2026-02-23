import csv
import os

#CSV creator for the programs

def create_csv_program(filename, fieldnames):
    if not os.path.exists(filename):
        with open(filename, "w", newline="") as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            csv_writer.writeheader()
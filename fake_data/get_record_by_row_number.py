# this file has to be in the same directory as the .xlsx sheet
import openpyxl
import sys

# run this file with 
#       python3 get_record_by_row_number.py filename.xlsx row_number
filename = str(sys.argv[1])
row_number = int(sys.argv[2])

# grab the first worksheet
wb = openpyxl.load_workbook(filename)
ws = wb[wb.sheetnames[0]]

header_row = list(ws.rows)[0]
record_row = list(ws.rows)[row_number-1]

# store in a dictionary
person = {}

for i in range(0, 39):
	person[header_row[i].value] = record_row[i].value

# print the dictionary
print(person)

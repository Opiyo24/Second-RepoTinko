import openpyxl

# Load the workbook
wb = openpyxl.Workbook()

sheet = wb.active

sheet_title = sheet.title
sheet_title = "Oporo"

print(f"This is the {sheet_title}")

cell_1 = sheet.cell(row=1, column=1)
cell_1.value
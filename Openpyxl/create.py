import openpyxl

wb = openpyxl.Workbook()

sh = wb.active

sh.title = "Oporo_1"

print(f"This is the worksheet {sh.title}")

A1 = sh['A1']
A2 = sh['A2']
B1 = sh['B1']
B2 = sh['B2']

A1.value = "NAME"
A2.value = "Oporo"

B1.value = "GRADE"
B2.value = "A"


wb.save("OPORO.xlsx")

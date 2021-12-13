import json
import pandas as pd

filename = input("Please enter the XLSX file name: ")
filename += ".xlsx" if not filename.endswith(".xlsx") else ""

df = pd.read_excel(filename, engine="openpyxl", dtype=object, header=None)

values = df.values.tolist()
header_row = values[0]
first_student = values[1]
the_dict = dict(zip(header_row, first_student))

print(json.dumps(the_dict, indent=4, ensure_ascii=False))

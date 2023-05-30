import sys
import pandas as pd
from datetime import datetime

# Read the data from the Excel file and fill any missing values with an empty string
df = pd.read_excel('biweekly.xlsx', header=None).fillna('')
# Convert the data to a CSV file
df.to_csv('example.csv', index=False)

employeeList = ["Michael Scott", "Jim Halpert", "Pam Beesly", "Dwight Schrute","Angela Martin","Stanley Hudson",
    "Phyllis Vance","Kevin Malone","Oscar Martinez","Meredith Palmer","Ryan Howard","Kelly Kapoor","Andy Bernard",
    "Darryl Philbin","Toby Flenderson","Creed Bratton","Erin Hannon","Holly Flax","Jan Levinson","Roy Anderson"]

characters = [

]


df= pd.read_csv("example.csv")
# print(df)
# Get the list of names and dates from the command line arguments
args = sys.argv[2:]
names_and_dates_and_payCodeWithHours = [args[i:i+3] for i in range(0, len(args), 3)]
# print(f"{names_and_dates[0][1]} is of type: {type(names_and_dates[0][1])}")

# Loop through each name and date combination
for name, date, payCodeWithHour in names_and_dates_and_payCodeWithHours:
    # Find the row with the given name
    employeeRow = df.index[df.iloc[:, 0].astype(str).str.contains(name, na=False, case=False)].tolist()


    if len(employeeRow) == 0:
        print(f"No rows found for {name}")
        continue

    print(f"{date} is of type: {type(date)}")

    # Set the value of the cell with the given date to "hi"
    try:
        row_index, col_index = (df == date).values.nonzero()
        df.iloc[employeeRow[0]+1, col_index] = payCodeWithHour
    except KeyError:
        print(f"Invalid date: {date}")

outputFile = sys.argv[1]
# Save the updated data to the Excel file
df.to_excel(f'{outputFile}.xlsx', index=False, header=False)


### python3 script.py Cc Jonel "2023-03-12 00:00:00" "RGN 0600-1400"
###to run it cd to current directory python3 script.py nameOfYourDesiredOutPutFileWithoutExtenstion NameOfEmployee "YYYY-MM-DD 00:00:00"
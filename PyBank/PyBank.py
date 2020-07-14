#   PyBank
#   Create a Python script that analyzes the financial records
#   of your company using a file called budget_data.csv.
#   The dataset is composed of two columns: Date and Profit/Losses.
#   The output has to go to a file called ResultsAnalysis.

#   Dependencies
import csv
import os

#   Specify the file to load (Example 3.8)
csv_load = os.path.join("..", "Resources", "budget_data.csv")

#   Specify file to write to (Example 2.10)
txt_output = os.path.join("..", "Analysis", "ResultsAnalysis.txt")

#   Parameters for variables
TotalMonths = 0

#   Open and read csv (Example 3.1)
with open(csv_load) as budget_data:
    csvreader = csv.reader(budget_data)

    #   Read header row first (Example 3.1)
    csvheader = next(csvreader)







#   Results (In class Example)
results = (
    f"\nFinancial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {}\n"
    f"Total: ${}\n"
    f"Average Change: ${:.2f}\n"
    f"Greatest Increase in Profits: {} (${})\n"
    f"Greatest Decrease in Profits: {} (${})\n"
)

#   Print Results
print(results)

#   Export to File
with open(txt_output, "w") as text:
    text.write(results)

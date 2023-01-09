'''
Your task is to create a Python script that analyzes the records to calculate each of the following:
1. The total number of months included in the dataset
2. The net total amount of Profit/Losses over the entire period
3. The average of the changes in Profit/Losses over the entire period
4. The greatest increase in profits (date and amount) over the entire period
5. The greatest decrease in losses (date and amount) over the entire period

'''
import pandas as pd
from pathlib import Path

# csv path assignment
csv_path = Path("./PyBank/Resources/budget_data.csv")

# creating a dataframe from the csv file
budget_dataframe = pd.read_csv(csv_path)

# printing title and dotted lines for readability
print("Financial Analysis")
print("---------------------------")

# 1. The total number of months included in the dataset
total_months = budget_dataframe["Date"].size
total_months_results = f"Total Months: {total_months}"
print(total_months_results)

# 2. The net total amount of Profit/Losses over the entire period
net_total = budget_dataframe["Profit/Losses"].sum()
net_total_results = f"Total: ${net_total}"
print(net_total_results)

# 3. The average of the changes in Profit/Losses over the entire period
# finding the daily change by subtracting current day - previous day
daily_change = budget_dataframe["Profit/Losses"].diff()

# finding the average change by the mean
average_change = daily_change.mean()

average_change_results = f"Average Change: ${average_change: .2F}"
print(average_change_results)

# 4. The greatest increase in profits (date and amount) over the entire period
# finding the greatest increase value in the daily change values
greatest_increase = daily_change.max()

# creating a new column to make it easier to pull the accurate date
daily_change_column = budget_dataframe['Daily Change'] = daily_change

# finding the greatest increase value row by the greatest increase value
greatest_row = budget_dataframe.loc[budget_dataframe['Daily Change'] == greatest_increase]

# converting the date into a string and removing the index
increase_date = greatest_row["Date"].to_string(index=False)
greatest_increase_results = f"Greatest Increase in Profits: {increase_date} ${greatest_increase}"
print(greatest_increase_results)

# 5. The greatest decrease in losses (date and amount) over the entire period
# finding the greatest decrease value in the daily change values
greatest_decrease = daily_change.min()

# finding the greatest decrease value row by the greatest decrease value
greatest_row = budget_dataframe.loc[budget_dataframe['Daily Change'] == greatest_decrease]

# converting the date into a string and removing the index
decrease_date = greatest_row["Date"].to_string(index=False)
greatest_decrease_results = f"Greatest Decrease in Profits: {decrease_date} ${greatest_decrease}"
print(greatest_decrease_results)

# creating a new file and writing the results into it
with open("./PyBank/results_file.txt", 'w') as file:
    file.write("Financial Analysis\n")
    file.write("---------------------\n")
    file.write(f"{total_months_results}\n")
    file.write(f"{net_total_results}\n")
    file.write(f"{average_change_results}\n")
    file.write(f"{greatest_increase_results}\n")
    file.write(f"{greatest_decrease_results}\n")
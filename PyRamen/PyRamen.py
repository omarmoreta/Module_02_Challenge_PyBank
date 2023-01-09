# -*- coding: UTF-8 -*-
"""PyRamen Homework Starter."""

# @TODO: Import libraries
import csv
from pathlib import Path

# @TODO: Set file paths for menu_data.csv and sales_data.csv
menu_filepath = Path('./PyRamen/Resources/menu_data.csv')
sales_filepath = Path('./PyRamen/Resources/sales_data.csv')

# @TODO: Initialize list objects to hold our menu and sales data
menu = []
sales = []

# @TODO: Read in the menu data into the menu list
with open(menu_filepath, newline='') as file:
    csv_reader = csv.reader(file, delimiter=",")
    next(csv_reader)
    for row in csv_reader:
        menu.append(row)

# @TODO: Read in the sales data into the sales list
with open(sales_filepath, newline='') as file:
    csv_reader = csv.reader(file, delimiter=",")
    next(csv_reader)
    sales = list(csv_reader)

# @TODO: Initialize dict object to hold our key-value pairs of items and metrics
report = {}

# @TODO: Loop over every row in the sales list object
for sales_data in sales:
    # set variables to correct column
    quantity = int(sales_data[3])
    sales_item = sales_data[4]
    # if sales item is not in report dictionary append it as key and add dictionary of metrics as value
    if sales_item not in report:
        report[sales_item] = {"01-count": 0, "02-revenue": 0, "03-cogs": 0, "04-profit": 0 }
    # if sales item is in report then add the quantity 
    if sales_item in report:
        report[sales_item]["01-count"] += quantity 
        # iterate through the menu list of menu data   
        for menu_data in menu:
            # set variables to the correct column and calculate the profit
            menu_item = menu_data[0]
            price = float(menu_data[3])
            cost = float(menu_data[4])
            profit = price - cost
            # if the sales_item is equal to the menu item add the metrics in the report            
            if sales_item == menu_item:   
                report[sales_item]["02-revenue"] += price * quantity
                report[sales_item]["03-cogs"] += cost * quantity
                report[sales_item]["04-profit"] += profit * quantity

# title and dotted line for readability
print("PyRamen Sales Item Results")
print("------------------------------------")

# iterating the report and printing the key and values
for sales_item in report:
    print(f"{sales_item} : {report[sales_item]}")

# creating a new file and writing the results into it
with open("./PyRamen/PyRamen_results.txt", 'w') as file:
    file.write("PyRamen Sales Item Results\n")
    file.write("------------------------------------\n")
    for sales_item in report:
        file.write(f"{sales_item} : {report[sales_item]}\n")
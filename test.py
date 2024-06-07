import csv
import random

data = [
    ['Year', 'Sales', 'Expenses'],
    ['2004',  1000,      400],
    ['2005',  1170,      460],
    ['2006',  660,       1120],
    ['2007',  1030,      540]
]

# Generate data for years 2008 to 2024
for year in range(2008, 2025):
    sales = random.randint(500, 1500)  # Random sales value between 500 and 1500
    expenses = random.randint(300, 1200)  # Random expenses value between 300 and 1200
    data.append([str(year), sales, expenses])

with open('sales.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)
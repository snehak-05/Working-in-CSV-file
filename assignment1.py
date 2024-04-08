import csv
from collections import defaultdict
def write_data_to_csv(data, filename):
    with open(filename, "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)
def read_data_from_csv(filename):
    data = []
    with open(filename, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)
    return data
def calculate_revenue_by_company(csv_file):
    revenue_by_company = defaultdict(int)
    revenue_by_year = defaultdict(int)
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        for row in reader:
            year, company, revenue = row
            revenue_by_company[company] += int(revenue)
            revenue_by_year[year] += int(revenue)
    return revenue_by_company, revenue_by_year
data = [
    ["year", "company", "revenue"],
    ["2015", "eka", "200000"],
    ["2016", "dvi", "100000"],
    ["2018", "tri", "50000"],
    ["2015", "chatur", "10000"],
    ["2016", "eka", "70000"],
    ["2015", "dvi", "19000"],
    ["2015", "tri", "45000"],
    ["2017", "chatur", "22000"],
    ["2017", "eka", "80000"],
    ["2017", "dvi", "88000"],
    ["2016", "tri", "15500"],
    ["2018", "chatur", "32000"],
    ["2019", "eka", "123000"],
    ["2019", "dvi", "167700"],
    ["2019", "tri", "48000"],
    ["2019", "chatur", "12000"],
]
filename = "data.csv"
write_data_to_csv(data, filename)
print("File created")
data = read_data_from_csv(filename)
print(data)
revenue_by_company, revenue_by_year = calculate_revenue_by_company(filename)
print("Revenue by Company:")
for company, revenue in revenue_by_company.items():
    print(f"{company}: {revenue}")
print("\nRevenue by Year:")
for year, revenue in revenue_by_year.items():
    print(f"{year}: {revenue}")
   
   
         



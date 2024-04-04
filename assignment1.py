import csv
data=[
    ["year","company","revenue"],
    ["2015","eka","200000"],
    ["2016","dvi","100000"],
    ["2018","tri","50000"],
    ["2015","chatur","10000"],
    ["2016","eka","70000"],
    ["2015","dvi","19000"],
    ["2015","tri","45000"],
    ["2017","chatur","22000"],
    ["2017","eka","80000"],
    ["2017","dvi","88000"],
    ["2016","tri","15500"],
    ["2018","chatur","32000"],
    ["2019","eka","123000"],
    ["2019","dvi","167700"],
    ["2019","tri","48000"],
    ["2019","chatur","12000"],
    ]
with open(data.csv,"w")as file:
          writer=csv.writer(file)
          writer.writerows(csv_file)
print("filecreated")
with open("data.csv","r") as csv_file:
    reader=csv.reader(csv_file)
    for row in reader:
        print(row)
    csv_file.close()
from collections import defaultdict
def read_file(csv_file):
    data=[]
    with open(csv_file,"r") as file:
        reader=csv.reader(file)
        for row in reader:
            data.append(row)
    return(data)
csv_file="data.csv"
data=read_file(csv_file)
print(data)
def calculate_revenue_by_company(csv_file):
    revenue_by_company = defaultdict(int)
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        next(reader)  
        for row in reader:
            _, company, revenue = row
            revenue_by_company[company] += int(revenue)
    return (revenue_by_company)
csv_file = 'data.csv'
revenue_by_company = calculate_revenue_by_company(csv_file)
for company, revenue in revenue_by_company.items():
    print(f"{company}: {revenue}")


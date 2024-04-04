import csv#to import a csv file 
data=[
    ["year","company","revenue"],#this block of code creates a list
    ["2015","eka","200000"],
    ["2016","dvi","100000"],# where every element represents a row 
    ["2018","tri","50000"],
    ["2015","chatur","10000"],# year,company,revenue
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
with open("data.csv","w")as file:#this line opens a file name data.csv in write mode
          writer=csv.writer(file)#these lines used to wrtie the content
          writer.writerows(data)#of data list in the csv file
print("filecreated")#this line prints file created when file create
with open("data.csv","r") as csv_file:#this line opens csv file name data in read mode
    reader=csv.reader(csv_file)#this line reads the content of the file data
    for row in reader:#this block will iterateover the list and print it
        print(row)
    csv_file.close()#this line closes the file
from collections import defaultdict#This line imports the defaultdict class from the collections mpodule defaultdict is a subclass of build in function dict class that automatically creates new entries for keys 
def read_file(csv_file):#function is defined with name read_file ans csv file is passed as an argument
    data=[] #this creates a empty list data
    with open(csv_file,"r") as file:#opens a csv file for reading
        reader=csv.reader(file)#this line reads the file
        for row in reader:#this block iterate over the rows and append data in data
            data.append(row)
    return(data)#it will return data as output 
csv_file="data.csv"#assigning data.csv to csv_file
data=read_file(csv_file)#function calling statement
print(data)#prints data 
def calculate_revenue_by_company(csv_file):#function is defined with name calculate_revenue_by_company and csv_file as argument is passed 
    revenue_by_company = defaultdict(int)#this will store total revenue for the company 
    with open(csv_file, 'r') as file:#opens csv file in read mode
        reader = csv.reader(file)#reading csv file
        next(reader)  #This line skips the header row of the CSV file.
        for row in reader:#loops iterates over rows of csv file 
            year , company, revenue = row#three varibles are assigned values in rows 
            revenue_by_company[company] += int(revenue)#adds total revenue to correspong company 
    return (revenue_by_company)#function returns revenue_by_company as output 
csv_file = 'data.csv'#data.csv assing to csv_file
revenue_by_company = calculate_revenue_by_company(csv_file)#function calling statement
for company, revenue in revenue_by_company.items():#This loop iterates over each key-value pair in the revenue_by_company dictionary and prints the company name along with its total revenue.
    print(f"{company}: {revenue}")




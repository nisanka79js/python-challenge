import os
import csv

from zmq import PROTOCOL_ERROR_ZMTP_MALFORMED_COMMAND_INITIATE
#csv file path
filepath ="C:\\Users\\Samanthi Nisanka\\OneDrive\\Desktop\\bootcamp\\python-challenge\\PyBank\\Resources\\budget_data.csv"
#csvfile = open(filepath,"r")
#import modules

#import os
#import csv

#set path to csv file in PyBank
#file_path = ""C:\Users\Samanthi Nisanka\Desktop\bootcamp\python-challenge\PyBank\Resources\budget_data.csv"

#store data
months=[]
profit=[]
monthly_change=[]

#variables
count = 0
total_net = 0
highest_increase=0
highest_decrease=0
j=0
#open the csv
 
with open (filepath, 'r' ) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    for row in csvreader:

#count number of months

        count = count + 1
        months.append(row[0])
        #profit =[18900092,-34482,09988,999]
        #profit[2]

#calculate profit
        profit.append(int(row[1]))
        total_net = total_net + int(row[1])
        #j=j+1
        if len(profit)>=1:
            current_change = profit[count-1]-profit[count-2]
            if current_change > highest_increase:
                increase_month = row[0]
                highest_increase= current_change

            if current_change<highest_decrease:
                increase_month=row[0]
                highest_decrease=current_change
    
    for row in len(profit):
        profit_loss_change = profit[row+1]-profit[row]
        monthly_change = profit.append

print(highest_increase)
print(highest_decrease)


print("----------------------------------------------------------")
print("Financial Analysis")
print("----------------------------------------------------------")

print("Total Months: " + str(count))
print("Total Net: " + "$" + str(total_net))

    
    
# with open('Financial_Analysis.txt', 'w') as text:
     
#     text.write("----------------------------------------------------------\n")
#     text.write("  Financial Analysis"+ "\n")
#     text.write("----------------------------------------------------------\n\n")
#     text.write("    Total Months: " + str(count) + "\n")
#     text.write("    Total Profits: " + "$" + str(total_net) +"\n")
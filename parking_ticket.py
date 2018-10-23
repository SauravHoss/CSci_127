#Saurav Hossain
#09/21/18
#Parking Tickets


#Taken from lab and edited
#Import pandas for reading and analyzing CSV data:
import pandas as pd

x = input()   
ss = input()
      
tickets = pd.read_csv(x)
print("The 10 worst offenders are:")
print(tickets[ss].value_counts()[:10]) #Print out the dataframe
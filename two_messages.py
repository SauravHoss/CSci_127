#Saurav Hossain
#09/04/18
#Prints two copies, 1 character per line

x = input()

for i in range(len(x)):
  print(x[i:i+1] + " " + x[i:i+1]) 
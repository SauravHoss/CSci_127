#Saurav Hossain
#08/29/18
#Prints GC amount in a string in % as decimal

z = input()

c = 0

for i in range(len(z)):
 if(z[i] == "G" or z[i] == "C"):
 	c = c + 1 
print (len(z))
print (c / len(z))
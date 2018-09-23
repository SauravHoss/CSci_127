#Saurav Hossain 
#09/08/18 
#Word Splits

x = input()

y = x.split()
c = len(y)
d = 0

for i in y:
  if i[-1:] == "s":
    d = d + 1

print (c, d/c)
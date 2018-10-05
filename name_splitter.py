#Saurav Hossain
#09/21/18
#Name Splitter

y = input()
f = str(y)
x = f.split(";")

for i in x:
  c = str(i)
  z = c.split(",")
  for i in range(1):
    print(z[1] + z[0])
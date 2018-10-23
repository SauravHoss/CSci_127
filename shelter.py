#Saurav Hossain
#09/21/18
#Shelter

import matplotlib.pyplot as plt
import pandas as pd

x = input()
y = input()

fcg = pd.read_csv(x)
fcg['Fraction Children'] = fcg['Total Children in Shelter']/fcg['Total Individuals in Shelter']
fcg.plot(x = 'Date of Census', y = 'Fraction Children')
fig = plt.gcf()
fig.savefig(y)
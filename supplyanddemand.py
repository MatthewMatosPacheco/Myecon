
import matplotlib.pyplot as plt

import numpy as np

demand = np.arange(1000,200,-125)#x axis
price1= np.arange(500,1200,100)#y axis

demand2= np.arange(1600,800,-125)#x axis
price2= np.arange(400,1100,100) #yaxis
supply= np.arange(500,1400,50)
price_supply= np.arange(400,1300,50)
plt.figure(figsize=(10,7))
#plot demand curve
plt.plot(demand,price1, 'dodgerblue', demand2,price2,'red', supply, price_supply,'grey', linewidth=5.0) #demand curve
plt.axis((0,1800,300,1400))# set axis limit

#labels
plt.xlabel('Quantity(Q)')
plt.ylabel('Price (P)')
#annotations

plt.annotate('D1',xy=(230,1120))
plt.annotate('D2',xy=(830,1020))
plt.annotate('Supply',xy=(1350,1270))
plt.annotate('Decrease \n in demand',xy=(850,650), arrowprops= dict(arrowstyle='->'), xytext=(1000,650))
plt.show()


#
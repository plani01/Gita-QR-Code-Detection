import numpy as np
import matplotlib.pyplot as plt
plt.style.use('bmh')

distanceData = np.loadtxt("C:/Users/plani/Documents/trash/10-20-2023, 15.04.52.csv",
                 delimiter=",")

x_axis = np.arange(0,len(distanceData),1) 

plt.plot(x_axis,distanceData)
plt.title('Distance Plot')
plt.xlabel('Valid Samples')
plt.ylabel('Distance From Camera(cm)')
plt.show()
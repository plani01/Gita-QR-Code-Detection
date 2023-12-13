import numpy as np
import matplotlib.pyplot as plt
plt.style.use('bmh')
testname = "carpetSlow1.csv"
distanceData = np.loadtxt("csvfiles" + "/" + "filtered_files" + "/" + "filtered_" + testname,delimiter=",")
#distanceData = np.loadtxt("csvfiles" + "/" + "alltests_csvFiles" + "/" + testname,delimiter=",")

x_axis = np.arange(0,len(distanceData),1) 

plt.plot(x_axis,distanceData)
plt.title('Distance Plot')
plt.xlabel('Valid Samples')
plt.ylabel('Distance From Camera(cm)')
plt.show()

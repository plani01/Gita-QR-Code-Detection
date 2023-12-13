#QR_DataReader.py#
#Author: Steven Miller
#Date created: December 13, 2023
#Purpose: to filter out data in CSV files from QR_RecordedVid_BATCH.py
#Used by: N/A
#Uses: numpy,os,datetime
#references:
#https://stackoverflow.com/questions/2363731/how-to-append-a-new-row-to-an-old-csv-file-in-python
#https://stackoverflow.com/questions/5927180/how-do-i-remove-all-zero-elements-from-a-numpy-array
#https://numpy.org/doc/stable/user/how-to-io.html
#https://numpy.org/doc/stable/reference/generated/numpy.savetxt.html
#https://numpy.org/doc/stable/reference/generated/numpy.array.html
#https://www.shecodes.io/athena/2142-converting-an-integer-to-string-in-python#:~:text=For%20example%2C%20if%20you%20have,a%20%3D%20str(5)%20.&text=This%20would%20output%20'5'%20.,like%20a%20%3D%20'5'%20.
#https://numpy.org/doc/stable/reference/generated/numpy.average.html
#https://numpy.org/doc/stable/reference/generated/numpy.min.html
#chatgpt

import numpy as np
import os
from datetime import datetime
#change directory to whatever your directory name is
root = "csvfiles"
directory = "alltests_csvFiles"
#create directory
if not os.path.exists(root + "/" +"filtered_files"):
    os.mkdir(root + "/" +"filtered_files")
#go through every csv file in the specified directory
for file in sorted(os.listdir(root+ "/" + directory)):
    filename = "filtered_" + file
    path = root + "/" +"filtered_files" + "/" + filename
    #declare np array
    array_values = np.genfromtxt(root + "/" + directory + "/" + file,delimiter=",", usemask=True)
    array_values = array_values[array_values != 0]
    array_values = array_values[array_values < 180]
    array_values = array_values[array_values > 80]
    np.savetxt(path,array_values,delimiter = ",",fmt = "%1.3f")
    #with open(path, 'a') as file_descriptor:
     #   file_descriptor.write("\nAverage distance: \n")
     #   file_descriptor.write(str(np.average(array_values)))
     #   file_descriptor.write("\nMinimum distance: \n")
     #   file_descriptor.write(str(np.min(array_values)))
     #   file_descriptor.write("\nMaximum distance: \n")
     #   file_descriptor.write(str(np.max(array_values)))
print("program has finished")

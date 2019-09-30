import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from scipy.stats import linregress
import csv


ifile  = open('file_directory', "rb") # reads first column of data from directed path
jfile  = open('file_directory', "rb") # reads second column of data from directed path

reader = csv.reader(ifile, delimiter=',') # column separator
reader2 = csv.reader(jfile, delimiter=',')

header = reader.next()      # read first row as title
header2 = reader2.next()

column = header.index("column1_title")       #y input
column2 = header2.index("column2_title")     #x input

z = []
for row in reader:
    col = row[column]
    z.append(col)
nan = 'str_to_remove'
y0 = [i for i in z if nan not in i]         # remove '' string from the data column


u = []
for row2 in reader2:
    col2 = row2[column2]
    u.append(col2)
nan = 'str_to_remove'
x0 = [i for i in u if nan not in i]


y = list(map(float, y0))                    # return the list as float
x = list(map(float, x0))

print('y:', y)                              # print out the list in order to confirm
print('x:', x)
print('y:', len(y0))  
print('x:', len(x0))                        # print out the # elements in list to confirm


m = linregress(x,y)                         # slope, intercept, rvalue, pvalue, marginalerror
slope = m[0]                                # I wanted only slope in this graph, you could use other data
print('m:', slope)


plt.xlabel('x_axis')
plt.ylabel('y_axis')
plt.scatter(x,y, label='data_label')

z = np.polyfit(x,y,1)                       # generate a trend line for the scatterplot
p = np.poly1d(z)
plt.plot(x,p(x),"r--", alpha=0.3)

plt.text(np.mean(x),0.5,s= str(slope))      # print out the slope value on graph, *(x,y) coordinate should be changed along your values)
plt.legend()
plt.show()

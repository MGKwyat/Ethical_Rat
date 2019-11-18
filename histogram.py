import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import csv, sys
from scipy.stats import norm

ifile  = open(sys.argv[1], "rb")
reader = csv.reader(ifile,delimiter=';')

header = reader.next()
header = [x.strip(' ') for x in header]
column = header.index(sys.argv[2])

y0 = []
for row in reader:
    col = row[column]
    y0.append(col)
nan = 'nan'
y0 = [i for i in y0 if nan not in i]

y = list(map(float, y0))

max_value = max((y))
min_value = min((y))
print(len(y))

n,bins,patches = plt.hist(y,int(sys.argv[3]), facecolor='blue')
plt.xlabel(sys.argv[2])
plt.ylabel('y_axin label')
plt.show()

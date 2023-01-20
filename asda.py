import numpy as np
import matplotlib.pyplot as plt
import csv
import os

directory = '/Users/valentino/Desktop'


#1'000'000
Ue6 = []
te6 = []

with open("S1.csv", 'r') as file:
  csvreader = csv.reader(file)
  for row in csvreader:
    te6.append(row[0])
    Ue6.append(row[1])


Ue6.remove(Ue6[0])
te6.remove(te6[0])

Ue6_i = [float(u) for u in Ue6]
te6_i = [float(t) for t in te6]


plt.plot(te6_i[:][::10],Ue6_i[:][::10],".-",markersize=3)
plt.xlabel("Stromstaerke I[$A$]")
plt.ylabel("t [s]")
plt.title("")

#plt.show()

import tikzplotlib
tikzplotlib.save("S1.1.tex")

import matplotlib as mpl

plt.close()
mpl.rcParams.update(mpl.rcParamsDefault)



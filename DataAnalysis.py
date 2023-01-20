import csv
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pandas as pd

fig1, ax1 = plt.subplots()
fig2, ax2 = plt.subplots()
fig3, ax3 = plt.subplots()
fig4, ax4 = plt.subplots()
fig5, ax5 = plt.subplots()
fig6, ax6 = plt.subplots()
fig7, ax7 = plt.subplots()
fig8, ax8 = plt.subplots()


#1'000'000
Ue6 = []
te6 = []

with open("Spannung 1'000'000.csv", 'r') as file:
  csvreader = csv.reader(file)
  for row in csvreader:
    te6.append(row[0])
    Ue6.append(row[1])


Ue6.remove(Ue6[0])
te6.remove(te6[0])

Ue6_i = [float(u) for u in Ue6]
te6_i = [float(t) for t in te6]


#6800
U68 = []
t68 = []

with open("Spannung 6800.csv", 'r') as file:
  csvreader = csv.reader(file)
  for row in csvreader:
    t68.append(row[0])
    U68.append(row[1])


U68.remove(U68[0])
t68.remove(t68[0])

U68_i = [float(u) for u in U68]
t68_i = [float(t) for t in t68]

#4700
U47 = []
t47 = []

with open("Spannung 4700.csv", 'r') as file:
  csvreader = csv.reader(file)
  for row in csvreader:
    t47.append(row[0])
    U47.append(row[1])


U47.remove(U47[0])
t47.remove(t47[0])

U47_i = [float(u) for u in U47]
t47_i = [float(t) for t in t47]

#2200
U22 = []
t22 = []

with open("Spannung 2200.csv", 'r') as file:
  csvreader = csv.reader(file)
  for row in csvreader:
    t22.append(row[0])
    U22.append(row[1])


U22.remove(U22[0])
t22.remove(t22[0])

U22_i = [float(u) for u in U22]
t22_i = [float(t) for t in t22]

#1000
U10 = []
t10 = []

with open("Spannung 1000.csv", 'r') as file:
  csvreader = csv.reader(file)
  for row in csvreader:
    t10.append(row[0])
    U10.append(row[1])


U10.remove(U10[0])
t10.remove(t10[0])

U10_i = [float(u) for u in U10]
t10_i = [float(t) for t in t10]

#470
U4_7 = []
t4_7 = []

with open("Spannung 470.csv", 'r') as file:
  csvreader = csv.reader(file)
  for row in csvreader:
    t4_7.append(row[0])
    U4_7.append(row[1])


U4_7.remove(U4_7[0])
t4_7.remove(t4_7[0])

U4_7_i = [float(u) for u in U4_7]
t4_7_i = [float(t) for t in t4_7]

#220
U2_2 = []
t2_2 = []

with open("Spannung 220.csv", 'r') as file:
  csvreader = csv.reader(file)
  for row in csvreader:
    t2_2.append(row[0])
    U2_2.append(row[1])


U2_2.remove(U2_2[0])
t2_2.remove(t2_2[0])

U2_2_i = [float(u) for u in U2_2]
t2_2_i = [float(t) for t in t2_2]

#100
U1 = []
t1 = []

with open("Spannung 100.csv", 'r') as file:
  csvreader = csv.reader(file)
  for row in csvreader:
    t1.append(row[0])
    U1.append(row[1])


U1.remove(U1[0])
t1.remove(t1[0])

U1_i = [float(u) for u in U1]
t1_i = [float(t) for t in t1]

def meandep(a,e,U): #always + 0.02

    a1 = a*50
    e1 = e*50 

    mn = []

    mn.append(U[a1:e1])
     
    mnn = sum(mn[0])/len(mn[0])
    
    return mnn


def dqm(U,meandep,a,e):
  qA =  []

  a1 = a*50
  e1 = e*50 

  for i in range(0,len(U[a1:e1])):
    s = (U[a1:e1][i] - meandep)**2

    qA.append(s)
  
  DQM = sum(qA)/len(qA)

  return DQM

Z = [U1_i,U2_2_i,U4_7_i,U10_i,U22_i,U47_i,U68_i,Ue6_i]

for z in Z:
    print(len(z))

#plt.plot(t1_i[::50],U1_i[::50])
#plt.plot(t2_2_i[::50],U2_2_i[::50])
#plt.plot(t10_i[::50],U10_i[::50])
#plt.plot(t4_7_i[::50],U4_7_i[::50])
#plt.plot(t22_i[::50],U22_i[::50])
#plt.plot(t47_i[::50],U47_i[::50])
#plt.plot(t68_i[::50],U68_i[::50])
plt.plot(te6_i[::50],Ue6_i[::50])


plt.xlabel("t [s]")
plt.ylabel("Spannung U [$A$]")
plt.title("1 $F$")



import tikzplotlib
tikzplotlib.save("Spannung1e6muF.tex")

import matplotlib as mpl

plt.close()
mpl.rcParams.update(mpl.rcParamsDefault)



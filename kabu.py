# -*- coding: utf-8 -*-
from matplotlib import pyplot as plt
import numpy as np

#散布図を用意
x1 = np.random.rand(50)*0.7
y1 = 1.5*x1+np.random.rand(50)
z1 = np.array([1]*50)
data1 = np.array([x1,y1,z1]).T #.Tは転置

x2 = np.random.rand(50)*0.5 + 0.4
y2 = 0.5*x2+np.random.rand(50)
z2 = [-1]*50

data2 = np.array([x2,y2,z2]).T #.Tは転置

fig = plt.figure()

ax = fig.add_subplot(1,1,1)#重ねてプロットできるようにしている

ax.scatter(data1[:,0],data1[:,1], c='red')
ax.scatter(data2[:,0],data2[:,1], c='blue')


ax.set_title('scatter plot')
ax.set_xlabel('x(1)')
ax.set_ylabel('x(2)')

fig.show()

indexX1=0
indexX2=1
#赤、青両方のデータを結合してx(1)の値でソートする
bindData = np.r_[data1,data2][:,indexX1].argsort() #昇順にソートしたインデックス取得
sortedData = np.r_[data1,data2][bindData] 

zValue = 0
max = [0,0]
fig2 = plt.figure()
ax2 = fig2.add_subplot(1,1,1)
ax2.set_title('sum of class1 value')
ax2.set_xlabel('x(2)')
ax2.set_ylabel('value')

for i in range(100):
    zValue = zValue + sortedData[i,2]
    if ( fabs(zValue) > fabs(max[1])):
        max = [i,zValue]
    ax2.scatter(i,zValue)

#ax.axvline(x=sortedData[max[0],0],color="black")
ax.axhline(y=sortedData[max[0],indexX2],color="black")
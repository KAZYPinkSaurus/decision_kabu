# -*- coding: utf-8 -*-

import random
import math
from matplotlib import pyplot as plt
import numpy as np

#bootstrap
#引数：一次元のリスト
#返り値：一次元のリスト
def bootstrap(dataArray):
    arrayColumn = len(dataArray)
    outArray = np.zeros((arrayColumn,len(dataArray[0])))
    for i in range(arrayColumn):
        outArray[i] = dataArray[random.randint(0,arrayColumn - 1)]
    return outArray


#境界線を求める
#引数：２種類のデータ
#返り値：X、Yの境界線の値
def learnBorder(data1,data2): 
    Xmax = 0
    Ymax = 0
    for k in [0,1]:
       # 昇順ソート
        bindData = np.r_[data1,data2][:,k].argsort()
        sortedData = np.r_[data1,data2][bindData] 
        zValue = 0
        max = [0,0]   
        for i in range(len(sortedData)):
            zValue = zValue + sortedData[i,2]
            if ( math.fabs(zValue) > math.fabs(max[1])):
                max = [i,zValue]         
        if k == 0:
            Xmax = sortedData[max[0],k]
        else:
            Ymax = sortedData[max[0],k]
    return [Xmax,Ymax]

#複数回学習し、結果の境界線の座標リストを返す
#num:学習回数
def makeBorderList(data1,data2,num):
    outArray = np.zeros((num,2))
    for i in range(num):
        outArray[i] = learnBorder(bootstrap(data1),bootstrap(data2))
    return outArray
    

#学習して得られた境界線をもとにして、最終的な境界線を求める
#引数：X軸、Y軸における境界線のリスト
#返り値：座標リスト
def makeCoordinateData(Xborder,Yborder):
    coordinateData = np.array([[0.00]*1000,[0.00]*1000]).T
    for m in range(0,1000):
        Xresult = [0,10000000]
        result_y = 0
        for k in range(len(Yborder)):
            if m*0.0025 >= Yborder[k]:
                result_y = result_y + 1 
            else:
                result_y = result_y + -1
        for j in range(0,1000):
            result_x = result_y
            for i in range(len(Xborder)):
                if j*0.0015 <= Xborder[i]:
                    result_x = result_x + 1 
                else:
                    result_x = result_x + -1
            if math.fabs(result_x) <= math.fabs(Xresult[1]):
                Xresult = [j*0.0015,result_x]
                if (j % 1000) == 0:         
                    print(j,m)
                coordinateData[m,:] = [j*0.0015,m*0.0025] 
    return coordinateData

##散布図を用意
#x1 = np.random.rand(50)
#y1 = 1*x1+np.random.rand(50)*1.1+1.0
#z1 = np.array([1]*50)
#data1 = np.array([x1,y1,z1]).T #.Tは転置
#
#x2 = np.random.rand(50)
#y2 = 1*x2+np.random.rand(50)*1.1
#z2 = [-1]*50
#
#data2 = np.array([x2,y2,z2]).T #.Tは転置

numOfLearn = 2000 #学習回数
L=makeBorderList(data1,data2,numOfLearn)   
K = makeCoordinateData(L[:,0],L[:,1])
plt.figure()
plt.hold(True)
plt.title('decision_kabu')
plt.xlabel('x(1)')
plt.ylabel('x(2)')
plt.scatter(data2[:,0],data2[:,1], c='blue')
plt.scatter(data1[:,0],data1[:,1], c='red')
for i in range(1000):#各境界線の位置
    plt.scatter(L[i,0],0,color="green")
    plt.scatter(0,L[i,1],color="green")
plt.plot(K[:,0],K[:,1],color="black")

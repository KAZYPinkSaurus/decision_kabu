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
    print("Hello")
    for i in range(arrayColumn):
        outArray[i] = dataArray[random.randint(0,arrayColumn - 1)]
    return outArray

#どこでソートする？

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
    
    
#L=makeBorderList(data1,data2,30)   
#plt.figure()
#plt.hold(True)
#plt.scatter(data2[:,0],data2[:,1], c='blue')
#plt.scatter(data1[:,0],data1[:,1], c='red')
#for i in range(30):
#    plt.scatter(L[i,0],0,color="black")
#    plt.scatter(0,L[i,1],color="black")

    
    
    
   
Xborder = [2,2,3,2,3,2,3,2,3,2,3,2,3,4,3,2,3,2,4,5,3,2,2,3,4,5]
Yborder = [3,3,4,3,4,6,5,4,3,2,4,5,6,6,5,4,3,2,2,5,6,6,7,7,7,7]

##学習して得られた境界線をもとにして、最終的な境界線を求める
##引数：X軸、Y軸における境界線のリスト
##返り値：座標リスト
#def plotBorder(Xborder,Yborder):
#    coordinateData = np.array([[0]*500,[0,500]]).T
#    for m in range(0,500):
#        Xresult = [0,1000]
#        for j in range(0,500):
#            result = 0
#            for i in range(len(Xborder)):
#                if j*0.01 <= Xborder[i]:
#                    result = result + 1 
#                else:
#                    result = result + -1
#            for k in range(len(Yborder)):
#                if m*0.01 <= Yborder[k]:
#                    result = result + 1 
#                else:
#                    result = result + -1
#            if math.fabs(result) < math.fabs(Xresult[1]):
#                Xresult = [j*0.01,result]
#        print(Xresult[1]/(len(Xborder)+len(Yborder)))#確率
#        print(m*0.01) #y座標
#        #座標を突っ込む仕組みはまだ
#    return coordinateData
#    #これをプロットしていけばよさそう
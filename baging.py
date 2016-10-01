# -*- coding: utf-8 -*-

import random
import math
from matplotlib import pyplot as plt
import numpy as np

#bootstrap
#引数：一次元のリスト
#返り値：一次元のリスト
def bootstrap(dataArray):
    arrayLength = len(dataArray)
    list = [0]*arrayLength
    for i in range(arrayLength):
        list[i] = dataArray[random.randint(0,arrayLength - 1)]
    return list

#どこでソートする？

#境界線を求める
#引数：昇順にソートされたデータの座標とクラスの値（ともにリスト）
#返り値：境界線の値リストのリスト
def learnBorder(coordinate,value):
    zValue = 0
    Xmax = [0,0]   
    for i in range(100):
        zValue = zValue + coordinate[i,2]
        if ( math.fabs(zValue) < math.fabs(Xmax[1])):
            Xmax = [i,zValue]          
            #y軸ようにソートし直す######
    zValue = 0
    Ymax = [0,0]   
    for j in range(100):
        zValue = zValue + coordinate[j,2]
        if ( math.fabs(zValue) > math.fabs(Ymax[1])):
            Ymax = [j,zValue]
    return [Xmax[0],Ymax[0]]


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
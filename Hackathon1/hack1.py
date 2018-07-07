from matplotlib import pyplot as plt
from matplotlib import style
from scipy import stats
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
class A:
    def __init__(self):
        pass
    def Graph(self):
        a1 = pd.read_csv("fbData.csv")
        a2 = pd.read_csv("Instadata.csv")
        a3 = pd.read_csv("SnapData.csv")
        list1 = []
        list1 = a1["USER"]
        list2 = []
        list2 = a1["YEARS"]

        list3 = []
        list3 = a2["USER"]
        list4 = []
        list4 = a2["YEARS"]

        list5 = []
        list5 = a3["USER"]
        list6 = []
        list6 = a3["YEARS"]
        plt.title("Bar Graph")

        #ax = plt.subplot(111)
        #ax.bar(list2 - 0.2, list1, width=0.2, color='b', align='center')
        #ax.bar(list4, list3, width=0.2, color='r', align='center')
        #ax.bar(list6 + 0.2, list5, width=0.2, color='c', align='center')
        plt.plot(list2,list1,label= "FB",linewidth = 1)
        plt.plot(list4,list3,label = "INSTAGRAM",linewidth = 1.25)
        plt.plot(list6,list5,label = "SNAPCHAT",linewidth = 1.48)
        X = list2
        Y = list1
        dt = stats.linregress(X,Y)
        b1 = (dt[0])
        b0 = (dt[1])
        Y1 = []

        for x in X:
            y = b0 + (b1 * x)
            Y1.append(y)
        print("============")
        print(Y1)
        print("============")

        plt.plot(X,Y,"o",X,Y1)
        B = list4
        C = list3
        dt = stats.linregress(B, C)
        b1 = (dt[0])
        b0 = (dt[1])
        Y2 = []

        for x in B:
            y = b0 + (b1 * x)
            Y2.append(y)
        print("============")
        print(Y2)
        print("============")

        plt.plot(B, C ,"o", B, Y2)

        D = list6
        E = list5
        dt = stats.linregress(D, E)
        b1 = dt[0]

        b0 = (dt[1])
        Y3 = []

        for x in D:
            y = b0 + (b1 * x)
            Y3.append(y)
        print("============")
        print(Y3)
        print("============")

        plt.plot(D, E, "o", D , Y3 )


        #regression = LinearRegression()
        #
        #l = len(X)
        #X = X.reshape(l ,1)
        #reg = regression.fit(X ,Y) # We are providing Training Data
        #
        #Y1 = reg.predict(X)
        #print("******************")
        #print(Y1)
        #print("******************")
        #mse = reg.score(X,Y)
        #print("******************")
        #print(mse)
        #print("******************")
        #plt.grid(True)
        plt.ylabel('USERS')
        plt.xlabel('YEARS')
        plt.legend()
        plt.grid(True)
        plt.show()
s1 = A()
s1.Graph()
##list4,list3,list6,list5,
#
#
#
#
##
"""TEAM
NIKHIL BAJAJ
ARUNAV GOEL
"""


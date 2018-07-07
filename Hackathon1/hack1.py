from matplotlib import pyplot as plt
from matplotlib import style
from scipy import stats
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics

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

        ax = plt.subplot(111)
        ax.bar(list2 - 0.2, list1, width=0.2, color='b', align='center')
        ax.bar(list4, list3, width=0.2, color='r', align='center')
        ax.bar(list6 + 0.2, list5, width=0.2, color='c', align='center')
        plt.plot(list2,list1,label= "FB",linewidth = 2)
        plt.plot(list4,list3,label = "INSTAGRAM",linewidth = 3)
        plt.plot(list6,list5,label = "SNAPCHAT",linewidth = 4)
        X =[list2,list4,list6]
        Y = [list1,list3,list5]
        #dt = stats.linregress(X,Y)
        #print(dt[0])
        #print(dt[1])
        #plt.plot(X,Y,"ro")
        from sklearn.linear_model import LinearRegression
        from sklearn.metrics import mean_squared_error

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
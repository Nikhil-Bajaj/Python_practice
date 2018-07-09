import time
import pandas as pd
from scipy import stats
from matplotlib import pyplot as plt

class A:
    def __init__(self):
        pass
    @classmethod
    def Graph(cls):

        a1 = pd.read_csv("fb1.csv")

        a2 = pd.read_csv("Insta.csv")

        a3 = pd.read_csv("Snap.csv")
        list1 = []
        list1 = a1["%Growth of USERS"]
        list2 = []
        list2 = a1["YEARS"]

        list3 = []
        list3 = a2["%Growth of USERS"]
        list4 = []
        list4 = a2["YEARS"]

        list5 = []
        list5 = a3["%Growth of USERS"]
        list6 = []
        list6 = a3["YEARS"]
        plt.title("Bar Graph")

        #ax1 = plt.subplot(111)
        #ax1.bar(list2 - 0.2, list1, width=0.2, color='b', align='center')
        #ax1.bar(list4, list3, width=0.2, color='r', align='center')
        #ax1.bar(list6 + 0.2, list5, width=0.2, color='c', align='center')
        #plt.plot(list2, list1, label="FB Actual", linewidth=1)
        #plt.plot(list4, list3, label="INSTAGRAM Actual", linewidth=1.25)
        #plt.plot(list6, list5, label="SNAPCHAT Actual", linewidth=1.48)
        X = list2
        Y = list1
        dt = stats.linregress(X, Y)
        b1 = (dt[0])
        b0 = (dt[1])
        Y1 = []

        for x in X:
            y = b0 + (b1 * x)
            Y1.append(y)

        h = 2012
        print("============")
        print(Y1)
        print("============")
        for m in range(1,len(Y1)-1):
            h = h + 1
            if Y1[m] >= Y1[m-1]:
                print("Trend of FB is increasing in year",h)
            else:
                print("trend of FB is decreasing in year",h)
        plt.plot(X, Y, "o", X, Y1)
        B = list4
        C = list3
        dt = stats.linregress(B, C)
        b1 = (dt[0])
        b0 = (dt[1])
        Y2 = []
        h =2014
        for x in B:
            y = b0 + (b1 * x)
            Y2.append(y)
        print("============")
        print(Y2)
        print("============")
        for n in range(3, len(Y2)-1):
            h = h + 1
            if Y2[n] >= Y2[n-1]:
                print("Trend of Insta is increasing in year ",h)
            else:
                print("trend of Insta is decreasing in year ",h)
        plt.plot(B, C, "o", B, Y2)
        h = 2015
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
        for o in range (4,len(Y3)-1):
            h = h + 1
            if (Y3[o]) >= (Y3[o-1]):
                print("Trend of Snapchat is increasing in year ",h)
            else:
                print("trend of Snapchat is decreasing in year ",h)
        plt.plot(D, E, "o", D, Y3)

        plt.ylabel('USERS')
        plt.xlabel('YEARS')
        plt.legend()
        plt.grid(True)
    @classmethod
    def end(self):
        endtime = time.time()
        print('end time is', endtime)
        return endtime
    @classmethod
    def show(self):
        plt.show()
starttime = time.time()
print('Starttime is',starttime)
A.Graph()
et = A.end()
A.show()

#endtime =time.time()
#print('end time is',endtime)
Totaltime = et - starttime
print("Time taken is",Totaltime)
"""
Team 
Nikhil  and Arunav
2nd Representation in %of User
"""
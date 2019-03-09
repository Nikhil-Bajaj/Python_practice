from tkinter import *
import threading
from tkinter import ttk
import pandas as pd
import csv
from difflib import SequenceMatcher
from matplotlib import pyplot as plt
import string
def g():

    def st1():

        c = var.get()
        df = pd.read_csv('{}.csv'.format(c), sep=",", usecols=(0, 16, 17, 18))
        pd.set_option('display.max_rows',800)
        print(df)
        #combo1['values']= df['Name']

        c1 = var1.get()
        df = pd.read_csv('{}.csv'.format(c1), sep=",", usecols=(0, 16, 17, 18))
        #combo3['values'] = df['Name']
        pd.set_option('display.max_rows', 800)
        print(df)
    def st():


        c = var.get()
        df = pd.read_csv('{}.csv'.format(c), sep=",", usecols=(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15, 16, 17, 18))
        #print(df)
        #combo1['values']= df['Name']


        #combo3['values'] = df['Name']
        #print(df)


        player1points = []
        player1matches = []

        firstplayer = w1.get()
        c2=firstplayer.upper()
        for y in range(len(df['Name'])):
            a = df['Name'][y]
            v = a.replace('*', ' ')
            ratio = SequenceMatcher(None, v, c2).ratio()
            if ratio >= 0.9:
                player1points.append(df['Testpoints'][y])
                player1points.append(df['Odipoints'][y])
                player1points.append(df['T20points'][y])
                player1matches.append(df['TESTSM'][y])
                player1matches.append(df['ODIM'][y])
                player1matches.append(df['T20M'][y])
                break
            else:
                pass
        print(player1points)
        c1 = var1.get()
        df = pd.read_csv('{}.csv'.format(c1), sep=",", usecols=(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15, 16, 17, 18))
        player2points = []
        player2matches = []
        secondplayer = w2.get()
        c3 = secondplayer.upper()
        #print(type(c3))

        for x in range(len(df['Name'])):
            a = df['Name'][x]
            v = a.replace('*', ' ')
            ratio = SequenceMatcher(None, v, c3).ratio()
            if ratio >= 0.9:

                player2points.append(df['Testpoints'][x])
                player2points.append(df['Odipoints'][x])
                player2points.append(df['T20points'][x])
                player2matches.append(df['TESTSM'][x])
                player2matches.append(df['ODIM'][x])
                player2matches.append(df['T20M'][x])
                break
            else:
                pass
        print(player2points)
        g=[1,2,3]
        plt.plot(g, player1points,'r', label="Player1", linewidth=1)
        plt.plot(g,player2points, 'c', label="Player2", linewidth=2)

        plt.title("Comparision on basis of points")
        plt.ylabel("Points ")
        plt.xlabel("Test,Odi and T20")
        plt.legend()
        plt.grid(True, color='g')
        plt.figure()
        g = [1, 2, 3]
        plt.plot(g, player1matches, 'r', label="Player1", linewidth=1)
        plt.plot(g, player2matches, 'c', label="Player2", linewidth=2)

        plt.title("Comparision on basis of matches played")
        plt.ylabel("Matches ")
        plt.xlabel("Test,Odi and T20")
        plt.legend()
        plt.grid(True, color='g')
        plt.show()




    window = Tk()
    var = StringVar(window)

    window.title("Welcome to CRICKETGAMBLING")
    lbl = Label(window, text="CRICKET GAMBLE", font=("Snap ITC", 50))
    lbl.grid(column=5, row=20)
    top_frame = Frame(window, bg='tomato', width=1600, height=50, pady=3).grid(row=50, columnspan=80)
    lb2 = Label(window, text='Player Comparison', font=("Comic Sans", 20))
    lb2.grid(row=80, column=5)
    blank1 = Label(window, text=" ").grid(row=90)
    country = Label(window, text='Select the country of the first player ', font=("Bradley Hand ITC", 20))
    country.grid(row=100, column=4)
    #w1 = Entry( window, font="Bradley Hand ITC", width=20)
    #w1.grid(row=100, column=9)

    var.set("Team1 ")
    combo = ttk.Combobox(window,textvariable=var , width=20,state='readonly')
    z = ['AFG', 'AUS', 'BAN', 'BER', 'CAN', 'EAF', 'ENG', 'HOK', 'IND', 'IRE', 'KEN', 'NAM', 'NEP', 'NZl', 'OMA',
         'PAK',
         'PNG', 'SAF', 'SCO', 'SRL', 'UAE', 'USA', 'WIN', 'ZIM']

    combo['values'] = z
    combo.grid(row=100, column=5)
    country2 = Label(window, text='Select the country of the Second player ', font=("Bradley Hand ITC", 20))
    country2.grid(row=130, column=4)

    var1 = StringVar(window)
    var1.set("Team2")
    combo2 = ttk.Combobox(window,textvariable= var1, width=20,state='readonly')
    z = ['AFG', 'AUS', 'BAN', 'BER', 'CAN', 'EAF', 'ENG', 'HOK', 'IND', 'IRE', 'KEN', 'NAM', 'NEP', 'NZl', 'OMA',
         'PAK',
         'PNG', 'SAF', 'SCO', 'SRL', 'UAE', 'USA', 'WIN', 'ZIM']

    combo2['values'] = z
    combo2.grid(row=130, column=5)

    btn = Button(window, text='Submit', command=st1).grid(row=140, column=5)

    player1 = Label(window, text='Enter the name of the first player ', font=("Bradley Hand ITC", 20))
    player1.grid(row=150, column=4)

    w1 = Entry(window)
    #try:
    #    # python 3.6
    #    var.trace_add('write', to_uppercase)
    #except AttributeError:
    ## python < 3.6
    #    var.trace('w', to_uppercase)
    w1.grid(row=150, column=5)
    #combo1 = ttk.Combobox(window, width=20)
    #combo1.grid(row=130, column=9)
    #output1 = Label(window)
    #output1.grid(row=120, column=9)
    blank1 = Label(window, text=" ").grid(row=140)



    #btn = Button(window, text='Submit', command=st).grid(row=170, column=5)
    player2 = Label(window, text='Enter the name of the second player ', font=("Bradley Hand ITC", 20))
    player2.grid(row=190, column=4)
    w2 = Entry(window)

    w2.grid(row=190, column=5)
    #combo3 = ttk.Combobox(window, width=20)
    #combo3.grid(row=190, column=9)
    #output1 = Label(window)

    btn3 = Button(window, text='Compare Players', command=st).grid(row=220, column=5)

    window.mainloop()

'''from tkinter import *
import threading
from tkinter import ttk
import pandas as pd
import csv
from difflib import SequenceMatcher
from matplotlib import pyplot as plt
import time
def g():
    def st():

        c = var.get()
        df = pd.read_csv('{}.csv'.format(c), sep=",", usecols=(0,1, 16, 17, 18))
        print(df)
        #combo1['values']= df['Name']

        c1 = var1.get()
        df = pd.read_csv('{}.csv'.format(c1), sep=",", usecols=(0,1, 16, 17, 18))
        #combo3['values'] = df['Name']
        print(df)


        player1 = []
        c2 = w1.get()
        for x in range(len(df['Name'])):
            a = df['Name'][x]
            v = a.replace('*', ' ')
            ratio = SequenceMatcher(None, v, c2).ratio()
            if ratio >= 0.5:
                # player1.append(v)
                player1.append(df['Testpoints'][x])
                player1.append(df['Odipoints'][x])
                player1.append(df['T20points'][x])

        player2 = []
        c3 = w2.get()
        for x in range(len(df['Name'])):
            a = df['Name'][x]
            v = a.replace('*', ' ')
            ratio = SequenceMatcher(None, v, c3).ratio()
            if ratio >= 0.5:
                # player1.append(v)
                player2.append(df['Testpoints'][x])
                player2.append(df['Odipoints'][x])
                player2.append(df['T20points'][x])

        plt.plot(player1, 'r', label="Player1", linewidth=1)
        plt.plot(player2, 'c', label="Player2", linewidth=2)
        # plt.bar(a,b,label="Dart",color='r',width=0.5)
        plt.title("Comparision")
        plt.xlabel("Points Player1")
        plt.ylabel("Points Player2")
        plt.legend()
        plt.grid(True, color='g')
        plt.show()

    window = Tk()
    window.title("Welcome to CRICKETGAMBLING")
    lbl = Label(window, text="CRICKET GAMBLE", font=("Snap ITC", 50))
    lbl.grid(column=5, row=20)
    top_frame = Frame(window, bg='tomato', width=1200, height=50, pady=3).grid(row=50, columnspan=80)
    lb2 = Label(window, text='Player Comparison', font=("Comic Sans", 20))
    lb2.grid(row=80, column=5)
    blank1 = Label(window, text=" ").grid(row=90)
    country = Label(window, text='Select the country of the first player ', font=("Bradley Hand ITC", 20))
    country.grid(row=100, column=4)
    #w1 = Entry( window, font="Bradley Hand ITC", width=20)
    #w1.grid(row=100, column=9)
    var = StringVar(window)
    var.set("AFG")
    combo = ttk.Combobox(window,textvariable=var , width=20,state='readonly')
    z = ['AFG', 'AUS', 'BAN', 'BER', 'CAN', 'EAF', 'ENG', 'HOK', 'IND', 'IRE', 'KEN', 'NAM', 'NEP', 'NZl', 'OMA',
         'PAK',
         'PNG', 'SAF', 'SCO', 'SRL', 'UAE', 'USA', 'WIN', 'ZIM']

    combo['values'] = z
    combo.grid(row=100, column=5)

    #btn = Button(window, text='Submit', command=st).grid(row=120, column=5)

    player1 = Label(window, text='Select the name of the first player ', font=("Bradley Hand ITC", 20))
    player1.grid(row=130, column=4)

    w1 = Entry(window)
    w1.grid(row=130, column=5)
    #combo1 = ttk.Combobox(window, width=20)
    #combo1.grid(row=130, column=9)
    #output1 = Label(window)
    #output1.grid(row=120, column=9)
    blank1 = Label(window, text=" ").grid(row=140)

    country2 = Label(window, text='Select the country of the Second player ', font=("Bradley Hand ITC", 20))
    country2.grid(row=150, column=4)
    var1 = StringVar(window)
    var1.set("AFG")
    combo2 = ttk.Combobox(window,textvariable= var1, width=20,state='readonly')
    z = ['AFG', 'AUS', 'BAN', 'BER', 'CAN', 'EAF', 'ENG', 'HOK', 'IND', 'IRE', 'KEN', 'NAM', 'NEP', 'NZl', 'OMA',
         'PAK',
         'PNG', 'SAF', 'SCO', 'SRL', 'UAE', 'USA', 'WIN', 'ZIM']

    combo2['values'] = z
    combo2.grid(row=150, column=5)

    #btn = Button(window, text='Submit', command=st).grid(row=170, column=5)
    player2 = Label(window, text='Select the name of the second player ', font=("Bradley Hand ITC", 20))
    player2.grid(row=190, column=4)
    w2 = Entry(window)
    w2.grid(row=190, column=5)
    #combo3 = ttk.Combobox(window, width=20)
    #combo3.grid(row=190, column=9)
    #output1 = Label(window)

    btn3 = Button(window, text='Compare Players', command=st).grid(row=220, column=5)
    window.mainloop()


'''
"""
    window = Tk()
    window.title("Welcome to CRICKETGAMBLING")
    lbl = Label(window, text="CRICKET GAMBLE", font=("Snap ITC", 50))
    lbl.grid(column=5, row=20)
    top_frame = Frame(window, bg='tomato', width=1600, height=50, pady=3).grid(row=50, columnspan=80)
    lb2 = Label(window, text='Player Comparison', font=("Comic Sans", 20))
    lb2.grid(row=80, column=5)
    blank1 = Label(window, text=" ").grid(row=90)
    country = Label(window, text='Select the country of the first player ', font=("Bradley Hand ITC", 20))
    country.grid(row=100, column=4)
    #w1 = Entry( window, font="Bradley Hand ITC", width=20)
    #w1.grid(row=100, column=9)
    var = StringVar(window)
    var.set("AFG")
    combo = ttk.Combobox(window,textvariable=var , width=20,state='readonly')
    z = ['AFG', 'AUS', 'BAN', 'BER', 'CAN', 'EAF', 'ENG', 'HOK', 'IND', 'IRE', 'KEN', 'NAM', 'NEP', 'NZl', 'OMA',
         'PAK',
         'PNG', 'SAF', 'SCO', 'SRL', 'UAE', 'USA', 'WIN', 'ZIM']

    combo['values'] = z
    combo.grid(row=100, column=5)

    btn = Button(window, text='Submit', command=st).grid(row=120, column=5)

    player1 = Label(window, text='Select the name of the first player ', font=("Bradley Hand ITC", 20))
    player1.grid(row=130, column=4)

    w1 = Entry(window)
    w1.grid(row=130, column=5)
    #combo1 = ttk.Combobox(window, width=20)
    #combo1.grid(row=130, column=9)
    #output1 = Label(window)
    #output1.grid(row=120, column=9)
    blank1 = Label(window, text=" ").grid(row=140)

    country2 = Label(window, text='Select the country of the Second player ', font=("Bradley Hand ITC", 20))
    country2.grid(row=150, column=4)
    var1 = StringVar(window)
    var1.set("AFG")
    combo2 = ttk.Combobox(window,textvariable= var1, width=20,state='readonly')
    z = ['AFG', 'AUS', 'BAN', 'BER', 'CAN', 'EAF', 'ENG', 'HOK', 'IND', 'IRE', 'KEN', 'NAM', 'NEP', 'NZl', 'OMA',
         'PAK',
         'PNG', 'SAF', 'SCO', 'SRL', 'UAE', 'USA', 'WIN', 'ZIM']

    combo2['values'] = z
    combo2.grid(row=150, column=5)

    btn = Button(window, text='Submit', command=st).grid(row=170, column=5)
    player2 = Label(window, text='Select the name of the second player ', font=("Bradley Hand ITC", 20))
    player2.grid(row=190, column=4)
    w2 = Entry(window)
    w2.grid(row=190, column=5)
    #combo3 = ttk.Combobox(window, width=20)
    #combo3.grid(row=190, column=9)
    #output1 = Label(window)

    btn3 = Button(window, text='Compare', command=st).grid(row=220, column=5)
    window.mainloop()
"""
from tkinter import *

from tkinter import ttk
import pandas as pd

from difflib import SequenceMatcher
import string

def tc():
    def st():
        c = var.get()
        df = pd.read_csv('CurrentPlayers{}.csv'.format(c), sep=",", usecols=(1, 17, 18, 19))
        pd.set_option('display.max_rows', 800)
        print(df)


    def st1():
        c1 = var1.get()
        df = pd.read_csv('CurrentPlayers{}.csv'.format(c1), sep=",", usecols=(1, 17, 18, 19))
        pd.set_option('display.max_rows', 800)
        print(df)


    def compare():
        c = var.get()
        df = pd.read_csv('CurrentPlayers{}.csv'.format(c), sep=",", usecols=(1, 17, 18, 19))
        c1 = var1.get()
        df = pd.read_csv('CurrentPlayers{}.csv'.format(c1), sep=",", usecols=(1, 17, 18, 19))

        p1 = w1.get()

        p2 = w2.get()
        p3 = w3.get()
        p4 = w4.get()
        p5 = w5.get()
        p6 = w6.get()
        p7 = w7.get()
        p8 = w8.get()
        p9 = w9.get()
        p10 = w10.get()
        p11 = w11.get()
        pl1= p1.upper()
        pl2 = p2.upper()
        pl3 = p3.upper()
        pl4 = p4.upper()
        pl5 = p5.upper()
        pl6 = p6.upper()
        pl7 = p7.upper()
        pl8 = p8.upper()
        pl9 = p9.upper()
        pl10 = p10.upper()
        pl11 = p11.upper()
        play1 = [pl1, pl2, pl3, pl4, pl5, pl6, pl7, pl8, pl9, pl10, pl11]

        print(play1)

        team1Select = []
        team2Select = []
        team1test = []
        team1odi = []
        team1t20 = []
        for r in range(0, 11):
            # a= int(input("Select Team 1:"))
            z = play1[r]

            # z = input('Enter name of player: ')

            for x in range(len(df['Name'])):
                a = df['Name'][x]
                v = a.replace('*', ' ')
                ratio = SequenceMatcher(None, v, z).ratio()
                if ratio >= 0.8:
                    team1Select.append(v)
                    team1test.append(df['Testpoints'][x])
                    team1odi.append(df['Odipoints'][x])
                    team1t20.append(df['T20points'][x])
                    break
        # TEAM1TEST = 0
        # TEAM1ODI = 0
        # TEAM1T20 = 0
        TEAM1TEST = sum(team1test)
        TEAM1ODI = sum(team1odi)
        TEAM1T20 = sum(team1t20)
        print(TEAM1ODI)
        print(TEAM1TEST)
        print(TEAM1T20)

        team2 = []
        p1 = v1.get()
        p2 = v2.get()
        p3 = v3.get()
        p4 = v4.get()
        p5 = v5.get()
        p6 = v6.get()
        p7 = v7.get()
        p8 = v8.get()
        p9 = v9.get()
        p10 = v10.get()
        p11 = v11.get()
        pl1 = p1.upper()
        pl2 = p2.upper()
        pl3 = p3.upper()
        pl4 = p4.upper()
        pl5 = p5.upper()
        pl6 = p6.upper()
        pl7 = p7.upper()
        pl8 = p8.upper()
        pl9 = p9.upper()
        pl10 = p10.upper()
        pl11 = p11.upper()
        play2 = [pl1, pl2, pl3, pl4, pl5, pl6, pl7, pl8, pl9, pl10, pl11]
        print(play2)

        team2Select = []
        team2test = []
        team2odi = []
        team2t20 = []

        for r in range(0, 11):
            z = play2[r]

            for x in range(len(df['Name'])):
                a = df['Name'][x]
                v = a.replace('*', ' ')
                ratio = SequenceMatcher(None, v, z).ratio()
                if ratio >= 0.9:
                    team2Select.append(v)
                    team2test.append(df['Testpoints'][x])
                    team2odi.append(df['Odipoints'][x])
                    team2t20.append(df['T20points'][x])
                    break
            # TEAM2 = 0
            # TEAM2TEST = 0
            # TEAM2ODI = 0
            TEAM2T20 = 0
            TEAM2TEST = sum(team2test)
            TEAM2ODI = sum(team2odi)
            TEAM2T20 = sum(team2t20)
            if TEAM1TEST > TEAM2TEST:
                output.config(text='Your Test Team 1 {} is better than Team 2 {} '.format(c, c1))
            else:
                output.config(text='Your Test Team 2 {} is better than Team 1 {} '.format(c1, c))
            if TEAM1ODI > TEAM2ODI:
                output1.config(text='Your Odi Team 1 {} is better than Team 2 {}'.format(c, c1))
            else:
                output1.config(text='Your Odi Team 2 {} is better than Team 1 {} '.format(c1, c))
            if TEAM1T20 > TEAM2T20:
                output2.config(text='Your T20 Team 1 {} is better than Team 2 {} '.format(c, c1))
            else:
                output2.config(text='Your T20 Team 2 {} is better than Team 1 {}'.format(c1, c))
            TEAM1 = TEAM1TEST + TEAM1ODI + TEAM1T20
            TEAM2 = TEAM2TEST + TEAM2ODI + TEAM2T20
            if TEAM1 > TEAM2:
                output3.config(text='On overall comparision Your Team 1 {} is better'.format(c))
            else:
                output3.config(text='On overall comparision Your Team 2 {} is better'.format(c1))


    window = Tk()
    window.geometry("1600x800")
    window.title("Welcome to CRICKETGAMBLING")
    # lbl = Label(window, text="CRICKET GAMBLE", font=("Snap ITC", 40))
    # lbl.grid(column=5, row=20)
    top_frame = Frame(window, bg='cyan', width=900, height=70, pady=2).grid(row=25, columnspan=20)
    lb2 = Label(window, text='Team Comparison', font=("Snap ITC", 30))
    lb2.grid(row=50, column=5)

    country = Label(window, text='Select the country for your First team ', font=("Bradley Hand ITC", 20))
    country.grid(row=60, column=4)

    var = StringVar(window)
    var.set("")
    combo = ttk.Combobox(window, textvariable=var, width=20, state='readonly')
    z = ['AFG', 'AUS', 'BAN', 'BER', 'CAN', 'EAF', 'ENG', 'HOK', 'IND', 'IRE', 'KEN', 'NAM', 'NEP', 'NZl', 'OMA',
         'PAK',
         'PNG', 'SAF', 'SCO', 'SRL', 'UAE', 'USA', 'WIN', 'ZIM']

    combo['values'] = z
    combo.grid(row=60, column=5)

    btn = Button(window, text='Submit', command=st).grid(row=65, column=5)

    player1 = Label(window, text='Enter the name of the 1st player ', font=("Bradley Hand ITC", 20))
    player1.grid(row=70, column=4)

    w1 = Entry(window)
    w1.grid(row=70, column=5)

    player2 = Label(window, text='Enter the name of the 2nd player ', font=("Bradley Hand ITC", 20))
    player2.grid(row=80, column=4)

    w2 = Entry(window)
    w2.grid(row=80, column=5)

    player3 = Label(window, text='Enter the name of the 3rd player ', font=("Bradley Hand ITC", 20))
    player3.grid(row=90, column=4)

    w3 = Entry(window)
    w3.grid(row=90, column=5)

    player4 = Label(window, text='Enter the name of the 4th player ', font=("Bradley Hand ITC", 20))
    player4.grid(row=100, column=4)

    w4 = Entry(window)
    w4.grid(row=100, column=5)
    player5 = Label(window, text='Enter the name of the 5th player ', font=("Bradley Hand ITC", 20))
    player5.grid(row=110, column=4)

    w5 = Entry(window)
    w5.grid(row=110, column=5)

    player6 = Label(window, text='Enter the name of the 6th player ', font=("Bradley Hand ITC", 20))
    player6.grid(row=120, column=4)

    w6 = Entry(window)
    w6.grid(row=120, column=5)

    player7 = Label(window, text='Enter the name of the 7th player ', font=("Bradley Hand ITC", 20))
    player7.grid(row=130, column=4)

    w7 = Entry(window)
    w7.grid(row=130, column=5)
    player8 = Label(window, text='Enter the name of the 8th player ', font=("Bradley Hand ITC", 20))
    player8.grid(row=140, column=4)

    w8 = Entry(window)
    w8.grid(row=140, column=5)

    player9 = Label(window, text='Enter the name of the 9th player ', font=("Bradley Hand ITC", 20))
    player9.grid(row=150, column=4)

    w9 = Entry(window)
    w9.grid(row=150, column=5)

    player10 = Label(window, text='Enter the name of the 10th player ', font=("Bradley Hand ITC", 20))
    player10.grid(row=160, column=4)

    w10 = Entry(window)
    w10.grid(row=160, column=5)
    player11 = Label(window, text='Enter the name of the 11th player ', font=("Bradley Hand ITC", 20))
    player11.grid(row=170, column=4)

    w11 = Entry(window)
    w11.grid(row=170, column=5)
    # combo1 = ttk.Combobox(window, width=20)
    # combo1.grid(row=130, column=9)
    # output1 = Label(window)
    # output1.grid(row=120, column=9)

    var1 = StringVar(window)
    var1.set("")
    combo2 = ttk.Combobox(window, textvariable=var1, width=20, state='readonly')
    z = ['AFG', 'AUS', 'BAN', 'BER', 'CAN', 'EAF', 'ENG', 'HOK', 'IND', 'IRE', 'KEN', 'NAM', 'NEP', 'NZl', 'OMA',
         'PAK',
         'PNG', 'SAF', 'SCO', 'SRL', 'UAE', 'USA', 'WIN', 'ZIM']

    country = Label(window, text='Select the country for your Second team ', font=("Bradley Hand ITC", 20))
    country.grid(row=60, column=7)

    combo2['values'] = z
    combo2.grid(row=60, column=8)

    btn = Button(window, text='Submit', command=st1).grid(row=65, column=8)

    player1 = Label(window, text='Enter the name of the 1st player ', font=("Bradley Hand ITC", 20))
    player1.grid(row=70, column=7)

    v1 = Entry(window)
    v1.grid(row=70, column=8)

    player2 = Label(window, text='Enter the name of the 2nd player ', font=("Bradley Hand ITC", 20))
    player2.grid(row=80, column=7)

    v2 = Entry(window)
    v2.grid(row=80, column=8)

    player3 = Label(window, text='Enter the name of the 3rd player ', font=("Bradley Hand ITC", 20))
    player3.grid(row=90, column=7)

    v3 = Entry(window)
    v3.grid(row=90, column=8)

    player4 = Label(window, text='Enter the name of the 4th player ', font=("Bradley Hand ITC", 20))
    player4.grid(row=100, column=7)

    v4 = Entry(window)
    v4.grid(row=100, column=8)
    player5 = Label(window, text='Enter the name of the 5th player ', font=("Bradley Hand ITC", 20))
    player5.grid(row=110, column=7)

    v5 = Entry(window)
    v5.grid(row=110, column=8)

    player6 = Label(window, text='Enter the name of the 6th player ', font=("Bradley Hand ITC", 20))
    player6.grid(row=120, column=7)

    v6 = Entry(window)
    v6.grid(row=120, column=8)

    player7 = Label(window, text='Enter the name of the 7th player ', font=("Bradley Hand ITC", 20))
    player7.grid(row=130, column=7)

    v7 = Entry(window)
    v7.grid(row=130, column=8)
    player8 = Label(window, text='Enter the name of the 8th player ', font=("Bradley Hand ITC", 20))
    player8.grid(row=140, column=7)

    v8 = Entry(window)
    v8.grid(row=140, column=8)

    player9 = Label(window, text='Enter the name of the 9th player ', font=("Bradley Hand ITC", 20))
    player9.grid(row=150, column=7)

    v9 = Entry(window)
    v9.grid(row=150, column=8)

    player10 = Label(window, text='Enter the name of the 10th player ', font=("Bradley Hand ITC", 20))
    player10.grid(row=160, column=7)

    v10 = Entry(window)
    v10.grid(row=160, column=8)
    player11 = Label(window, text='Enter the name of the 11th player ', font=("Bradley Hand ITC", 20))
    player11.grid(row=170, column=7)

    v11 = Entry(window)
    v11.grid(row=170, column=8)




    btn3 = Button(window, text='COMPARE', command=compare).grid(row=190, column=5)
    output = Label(window, text=' ', font=("Snap ITC", 10))
    output.grid(row=210, column=5)
    output1 = Label(window, text=' ', font=("Snap ITC", 10))
    output1.grid(row=230, column=5)

    output2 = Label(window, text=' ', font=("Snap ITC", 10))
    output2.grid(row=240, column=5)
    output3 = Label(window, text=' ', font=("Snap ITC", 10))
    output3.grid(row=250, column=5)

    window.mainloop()

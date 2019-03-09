import os

z = ['AFG', 'AUS', 'BAN', 'BER', 'CAN', 'EAF',
     'ENG', 'HOK', 'IND', 'IRE', 'KEN', 'NAM', 'NEP', 'NED', 'NZL', 'OMA',
     'PAK', 'PNG', 'SCO', 'SAF', 'SRL', 'UAE', 'USA', 'WIN', 'ZIM']
def removalcsv():
    print("Cleanup Started")
    for l in z:
        try:
            os.remove("{}.csv".format(l))
            os.remove("{}names.csv".format(l))
            os.remove("CurrentPlayers{}.csv".format(l))
        except:
            pass
    print("Cleaup Fininshed")

import pandas as pd
import os
def current():
    z = ['AFG', 'AUS', 'BAN', 'BER', 'CAN', 'EAF', 'ENG', 'HOK', 'IND', 'IRE', 'KEN', 'NAM', 'NEP', 'NZl', 'OMA', 'PAK',
             'PNG', 'SAF', 'SCO', 'SRL', 'UAE', 'USA', 'WIN', 'ZIM']
    print("Current Players are being selected!!Please wait")
    for x in z:
        data = pd.read_csv('{}.csv'.format(x), sep=",", usecols=(0, 1,  5,  11, ))
        #print(data)
        str1 = data['Name'].tolist()
        #print(str1)

        currentplayers = []
        notcurrentplayers = []
        for i in range(0, len(str1)):
            if str1[i].endswith('*'):
                currentplayers.append(str1[i])
            else:
                notcurrentplayers.append(str1[i])

        #print(currentplayers)
        #print(len(currentplayers))

        my_df = pd.DataFrame(data=currentplayers, columns=['Name'])
        my_df.to_csv('{}names.csv'.format(x), index=False, encoding='utf-8')

        df1 = pd.read_csv('{}names.csv'.format(x))
        df2 = pd.read_csv('{}.csv'.format(x))
        output = pd.merge(df1, df2, how="inner", on="Name")  # column_name should be common in both dataframe
        # how represents type of intersection. In your case it will be inner(INNER JOIN)
        output['count'] = output.groupby('Name')['Name'].transform('size')  # pandas query
        final_output = output.drop_duplicates()  # It will remove duplicate rows
        #print(output)
        output.to_csv('CurrentPlayers{}.csv'.format(x))
        #os.remove("{}names.csv".format(x))
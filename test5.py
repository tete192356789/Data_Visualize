import numpy as np
import pandas as pd
 
# creating a dataframe
df = pd.read_csv('Superstore.csv',encoding ='windows-1252')

'''df = pd.DataFrame({'Name': ['Raj', 'Akhil', 'Sonum', 'Tilak', 'Divya', 'Megha','Raj','Raj','Sonum','Sonum'],
                   'Age': [20, 22, 21, 19, 17, 23,15,16,50,30],
                   'Rank': [1, np.nan, 8, 9, 4, np.nan,8,6,4,1]})'''
 
# printing the dataframe
'''print('DATAFRAME')
df_sort=df.sort_values(by=['Customer ID','Ship Mode'], ascending=False)
print(df_sort[['Customer ID','Ship Mode']])'''
#ex_list = df_sort[['Ship Mode','Customer ID']].values.tolist()
#newew = df.groupby(['Category','Customer ID'],sort = True)['Ship Mode'].count()
#gk = df.groupby(['State', 'Ship Mode']).median().reset_index().State

#print(df.loc[df['State'] == 'Alabama']['Ship Mode'])

print(df['Region'])
item = []
for i in df['Region']:
    item.append(i)

print(item)
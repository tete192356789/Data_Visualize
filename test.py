import csv
import pandas as pd
import json
import datetime
from datetime import datetime


df =pd.read_csv('Superstore.csv', encoding='windows-1252')



# df['Ship Date'] =  pd.to_datetime(df['Ship Date']).astype(str)
dd = df.groupby(['Order Date','Sales']).agg({'Sales':'sum'})
split = df['Ship Date'].str.split("/", expand = True)

df['Month Ship Date'] = split[1]
df['Date Ship Date'] = split[0]
df['Year Ship Date'] = split[2]
df.drop(columns = ['Ship Date'],inplace = True)

with open('metadata.json', 'r+') as read:
    metadata = json.load(read)
    #print(metadata['Superstore.csv'])

dt =pd.read_csv('data_test.csv', encoding='windows-1252')
dt_gb = dt.groupby(['Value'], as_index=False).agg({'Value':'sum'})





df1=pd.read_csv("popo.csv", encoding='windows-1252')
df2=pd.read_csv("Superstore_cut.csv", encoding='windows-1252')

full_df = pd.concat([df1,df2])
unique_df = full_df.drop_duplicates(keep= 'first').reset_index(drop = True)

# f = []
# for i in unique_df.loc[39]:
#   f.append(i)
# print(f)

res = df[~df.duplicated('City')]


dick = ['2222','region,city']

g1 = df['Category']
g2 = df['Sales']
gcc = pd.concat([g1,g2],axis =1 )
gcc = gcc[['Sales','Category']]
gbb = df.groupby(['Category'],as_index =False).agg('sum')
print(gbb['Category'])
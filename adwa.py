from vega_datasets import data
import pandas as pd
import altair as alt
from io import StringIO

new = data.cars()



#alt.data_transformers.enable('csv')
#url = 'file://path/to/data'

'''print(df)
chart = alt.Chart('https://vega.github.io/schema/vega-lite/v4.17.0.json').mark_line()


chart.serve()'''

df =pd.read_csv('popo.csv', encoding='windows-1252')
df2 =pd.read_csv('Superstore_cut.csv', encoding='windows-1252')

#print(len(df.columns))

output1 = pd.concat([df, df2], axis=0, ignore_index = True)

#output1.to_csv('merge.csv',index = False)



print(output1)

import csv

head = ['ID','Value','Date']
row = [{'ID': 'A','Value':2,'Date':'10/15/2020'},
        {'ID': 'A','Value':2,'Date':'10/15/2020'},
        {'ID':'B','Value':2,'Date':'10/4/2018'},
        {'ID':'C','Value':4,'Date':'25/8/2021'},
        {'ID':'D','Value':4,'Date':'2/1/2019'}]
fname = 'data_test.csv'
with open(fname,'w') as csvfile:
    csvw = csv.DictWriter(csvfile,fieldnames = head)
    csvw.writeheader()
    csvw.writerows(row)
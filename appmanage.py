from platform import java_ver
import pandas as pd
import datetime
from datetime import datetime
import os
import json
import hashlib

class manager():
    
    def load_file(self,file):
        self.file_name = file
        try:
            try:
                self.data =pd.read_csv(file, encoding='windows-1252')
            except:
                self.data = pd.read_csv(file,encoding='utf-8')
        except:
            self.data = pd.read_excel(file) 
        self.data = self.data.dropna()
        return self.data
    
    def md5_convert(self,filename):
       
        self.md5_fname = hashlib.md5(open(filename,'rb').read()).hexdigest()
        return self.md5_fname

    def load_json(self,fname):
        with open(fname, 'r') as read:
            self.data_json = json.load(read)
        return self.data_json

    def write_json(self,fname,col,data):
        with open('metadata.json', 'r') as read:
            load = json.load(read)
        
        load[fname][col] = data
            
        with open("metadata.json", "w") as read:
          
            #read.seek(0)
            json.dump(load,read,indent=4)
    def create_json(self,file):
        self.dict_list = {}
        

        # self.md5_file = manager.md5_convert(self,self.fp)
       

        #check data.json is exist.
        if not os.path.exists('metadata.json'):
            with open('metadata.json', 'w+') as write:
              json.dump(self.dict_list, write, ensure_ascii=False,indent =4)
        type_dict = {'dimension':[],'measurement':[]}
       
        with open('metadata.json', 'r+') as read:
            self.metadata = json.load(read)
            if file not in self.metadata:
                self.metadata[file]=type_dict
                read.seek(0)
                json.dump(self.metadata,read,indent = 4)


       # return self.file_json
        return self.metadata
    # split data date type and create new column in data
    def split_date(self,di,data):
        self.data = data
        self.data[di] =  pd.to_datetime(self.data[di]).astype(str)
        split = self.data[di].str.split("-", expand = True)
        print(split)
        self.data[f'Month {di}'] = split[1]
        self.data[f'Day {di}'] = split[2]
        self.data[f'Year {di}'] = split[0]
       # self.data.drop(columns = [di],inplace = True)
        
        return self.data

    def get_fj(self):
        return self.file_json


    def get_header(self,data):
        self.cols = data.columns.tolist()

        return self.cols

    def merge_data(self,data1,data2):
        self.merge_data = pd.concat([data1,data2], ignore_index = True)
        self.merge_data_non_dup = self.merge_data.drop_duplicates(keep =False).reset_index(drop = True)
        self.merge_data_non_dup.to_csv('merge.csv',index = False)
        self.merge_file =pd.read_csv('merge.csv', encoding='windows-1252')
        return self.merge_file
    def get_data(self):
        return self.data
    #check type of all header
    def check_header_type(self,data):
        self.cols = manager.get_header(self,data)
        self.type_dict = [{}]
        self.dimension_list = []
        self.measurement_list = []
        self.measure_header =[]
        self.dimension_header = []
        for i in self.cols:  
            try:
                ## check date
                if isinstance(datetime.strptime(str(data[i][0]), '%d/%m/%Y'),datetime) == True :
                    #to_dict = {i:type(datetime.strptime(str(self.data[i][0]), '%d/%m/%Y'))}
                    to_dict = {i:'date'}
                    self.type_dict[0][i] = 'date'
                    self.dimension_list.append(to_dict)
                    self.dimension_header.append(i)
            except:
                if i == 'Row ID':
                    to_dict = {i:data[i].dtypes}
                    self.type_dict[0][i]   = 'int'
                    self.dimension_list.append(to_dict)
                    self.dimension_header.append(i)
                elif i == 'Postal Code':
                    to_dict = {i:data[i].dtypes}
                    self.type_dict[0][i]   = 'str'
                    self.dimension_list.append(to_dict)
                    self.dimension_header.append(i)
                ##check float
                elif data[i].dtypes == float:
                    to_dict = {i:data[i].dtypes}
                    self.type_dict[0][i]   = 'float'
                    self.measurement_list.append(to_dict)
                    self.measure_header.append(i)
                #check int
                elif data[i].dtypes == 'int64':
                    to_dict = {i:data[i].dtypes}
                    self.type_dict[0][i]   = 'int'
                    self.measurement_list.append(to_dict)
                    self.measure_header.append(i)
            
                ##check str
                else:
                    to_dict = {i:data[i].dtypes}
                    self.type_dict[0][i]   = 'str'
                    self.dimension_list.append(to_dict)
                    self.dimension_header.append(i)
            
    
        
        
        return self.type_dict
        return self.dimension_list
        return self.measurement_list
        return self.measure_header
        return self.dimension_header
    def get_di(self):
        return self.dimension_header

    def get_mea(self):
        return self.measure_header
    #query data 
    def query_data(self,type_col,type_row,roller_row,roller_col,dimension,measure,data):
        p= []
        self.typer_col = type_col
        self.typer_row = type_row
     
        self.rr = roller_row
        self.cr = roller_col
        # print('roller from Row',self.rr)
        # print('roller from Column',self.cr)

        self.dimension_header=dimension
        self.measure_header = measure

        self.data2 =data.copy()

        for i in self.rr[0]:
            
            if i in self.dimension_header:
                if self.rr[0][i] == []:
                    empty_list = []
                    for k in self.data2[i]:
                        empty_list.append(k)
                    p.append(f"`{i}` in {empty_list}")
                else:
                    p.append(f"`{i}` in {self.rr[0][i]}")
            else:
                if self.rr[0][i] == []:
                    empty_list = []
                    for k in self.data2[i]:
                        empty_list.append(k)
                    p.append(f"`{i}` in {empty_list}")
                else:
                    p.append(f"`{i}`> {self.rr[0][i][0][0]} & `{i}`< {self.rr[0][i][0][1]}")


        for i in self.cr[0]:
            if i in self.dimension_header:
                if self.cr[0][i] == []:
                    empty_list = []
                    for k in self.data2[i]:
                        empty_list.append(k)
                    p.append(f"`{i}` in {empty_list}")
                else:
                    p.append(f"`{i}` in {self.cr[0][i]}")
            else:
                if self.cr[0][i] == []:
                    empty_list = []
                    for k in self.data2[i]:
                        empty_list.append(k)
                    p.append(f"`{i}` in {empty_list}")
                else:
                    p.append(f"`{i}`> {self.cr[0][i][0][0]} & `{i}`< {self.cr[0][i][0][1]}")
        
        p2 = " & ".join(p)
        print(p2)
        self.filter_x = self.data2.query(p2)
        print(self.filter_x)
        return self.filter_x
    def get_filter_x(self):
        return self.filter_x
    #Group-by data    
    def gb(self,tr,tc,hd,rr,cr,data):
        dict_type ={}
        self.typer_row =tr
        self.typer_col =tc
        self.dimension_head =hd
        self.rr =rr 
        self.cr =cr 
        self.data =data.copy()
        self.di = [i for i in list(cr[0].keys())+list(rr[0].keys()) if i in hd]
        print('++++++++++',rr,cr)
        for i in self.typer_row[0]:
            dict_type[i] = self.typer_row[0][i]
        for i in self.typer_col[0]:
            dict_type[i] = self.typer_col[0][i]  
        # print(self.di)
        # print(self.data.head)
        print(dict_type[i])
        print(self.di)
        non_dup_di = []
        for i in self.di:
            if i not in non_dup_di:
                non_dup_di.append(i)

        # if len(dict_type) == 0:
        #     self.gb = self.data.groupby(self.di,as_index=False).first()
        # else:
        self.gb = self.data.groupby(self.di,as_index=False).agg(dict_type)
        # print(self.gb.head())
        print(self.gb)
       
        return self.gb
     
    def get_gb(self):
        return self.gb

   
    
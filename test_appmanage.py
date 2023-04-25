import unittest
from appmanage import manager
import pandas as pd

class TestAppmanage(unittest.TestCase):

    def setUp(self):
        self.manager = manager()
        self.manager.load_file('Superstore.csv')

    def test_load_file(self):
        self.assertIsInstance(self.manager.load_file('Superstore.csv'),pd.core.frame.DataFrame)

    def test_get_header(self):
        df = pd.read_csv('Superstore.csv',encoding ='windows-1252')
        self.assertIsInstance(self.manager.get_header(df), list)
    
    def test_get_data(self):
        self.assertIsInstance(self.manager.get_data(), pd.core.frame.DataFrame)

    def test_check_header_type(self):
        df =pd.read_csv('Superstore.csv',encoding ='windows-1252')
        self.assertIsInstance(self.manager.check_header_type(df),list)

    def test_split_data(self):
        
        data = self.manager.load_file('Superstore.csv')
        di = 'Ship Date'
        self.assertIsInstance(self.manager.split_date(di,data),pd.core.frame.DataFrame)

    def test_create_json(self):
        file = 'metadata.json'
        self.assertIsInstance(self.manager.create_json(file),dict)

    def test_load_json(self):
        file = 'metadata.json'
        self.assertIsInstance(self.manager.create_json(file),dict)

    def test_gb(self):
        tr = [{'Sales':'sum'}]
        tc = [{}]
        hd =['Row ID', 'Order ID', 'Order Date', 'Ship Date', 'Ship Mode', 'Customer ID', 'Customer Name', 'Segment', 'Country/Region', 'City', 'State', 'Postal Code', 'Region', 'Product ID', 'Category', 'Sub-Category', 'Product Name']
        rr = [{'Category':[]}]
        cr = [{'Sales':[]}]
        data = self.manager.load_file('Superstore.csv')
        self.assertIsInstance(self.manager.gb(tr,tc,hd,rr,cr,data),pd.core.frame.DataFrame)

    def test_sum_gb(self):
        tr =[{'Value':'sum'}]
        tc=[{}]
        hd = ['ID','Value','Date']
        rr = [{'ID':[]}]
        cr = [{}]
        data = self.manager.load_file('data_test.csv')
        gb =self.manager.gb(tr,tc,hd,rr,cr,data)

        self.assertEqual(gb.at[0,'Value'],4)

    

    def test_mean_gb(self):
        tr =[{'Value':'mean'}]
        tc=[{}]
        hd = ['ID','Value','Date']
        rr = [{'ID':[]}]
        cr = [{}]
        data = self.manager.load_file('data_test.csv')
        gb =self.manager.gb(tr,tc,hd,rr,cr,data)
        print('++++++++',gb)
        self.assertEqual(gb.at[0,'Value'],2)
        
    #check lenght of row in union data
    def test_union_data(self):
        df1=pd.read_csv("popo.csv", encoding='windows-1252')
        df2=pd.read_csv("Superstore_cut.csv", encoding='windows-1252')
        merge_data = self.manager.merge_data(df1,df2)
        self.assertEqual(merge_data.shape[0],40)
    
    #check last row of union data
    def test_union_data2(self):
        df1=pd.read_csv("popo.csv", encoding='windows-1252')
        df2=pd.read_csv("Superstore_cut.csv", encoding='windows-1252')
        merge_data = self.manager.merge_data(df1,df2)
        last_row = [40, 'CA-2018-117415', '27/12/2018', '31/12/2018', 'Standard Class', 'SN-20710', 'Steve Nguyen', 'Home Office', 'United States', 'Houston', 'Texas', 77041, 'Central', 'FUR-CH-10004218', 'Furniture', 'Chairs', "Global Fabric Manager's Chair, Dark Gray", 212.058, 3, 0.3, -15.147]
        self.assertEqual(merge_data.loc[39].tolist(),last_row)

    def test_check_type(self):
        df = pd.read_csv('data_test.csv',encoding ='windows-1252')
        self.manager.check_header_type(df)
        di = ['ID','Date']
        di_head = self.manager.get_di()
        self.assertEqual(di_head,di)

    def test_split_date_len(self):
        df= pd.read_csv('data_test.csv',encoding ='windows-1252')
        split_date = self.manager.split_date('Date',df)
        print(split_date)
        sd_len = len(split_date.columns)
        self.assertEqual(sd_len,6)

  

if __name__ == "__main__":
    unittest.main()
    
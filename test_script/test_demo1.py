from generic.base_test import BaseTest
from generic.excel import Excel

class Test_Demo1(BaseTest):


    def test_demo1(self):
         #print("demo1")
         print(self.driver.title)
         v=Excel.get_data(self.xl_path,"Sheet1",1,1)
         print("from excel file: ",v)

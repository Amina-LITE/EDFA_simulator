import pandas as pd

# defining path as raw string not normal string!
file = r"database\LossTable.xlsx"


class excel_db:
    def __init__(self):
        self.excel_file = file
        self.excel_data = pd.read_excel(self.excel_file).fillna('')
         
    def run_excel_query(self, excel_query):
        return self.excel_data.query(excel_query)

    def getExcelData(self):
        return self.excel_data

    def setExcelFile(self, excel_file):
        self.excel_file = excel_file
    
    def getExcelFile(self):
        return self.excel_file
    

    




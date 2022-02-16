import openpyxl

class Excel:
    def get_data(path,sheet,row,col):
        wb = openpyxl.load_workbook(path)
        value = wb[sheet].cell(row,col).value
        print(value)
        return value
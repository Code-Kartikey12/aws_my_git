import pandas as pd
import xlrd as xd

data = pd.read_excel('D:/Home/Calculations/Life_Calculation.xlsx', sheet_name='Total Home Cost Calculator')
data_1=xd.sheet(data)
print(data_1)

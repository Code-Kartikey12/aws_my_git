import pandas as pd

series1 = pd.Series([1,2,3,4,5])
print(series1)

data_frame = pd.DataFrame({
    "Column1" : [1,2,3,4],
    "Column2" : ['a','b','c','d']
})
print(data_frame)

items = [['iphone X', 70000],['iphone XR',50000],['iphone 7', 30000]]
price_table = pd.DataFrame(items, columns=['Phone', 'price'], dtype='float')
print(price_table)
price_des = price_table.describe()
print(price_des)
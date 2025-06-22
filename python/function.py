import pandas as pd

data_object = pd.DataFrame({
    "customer_id": [1, 2, 3, 4],
    "name": ["rahul", "rohit", "shyam", "ravi"]
})

data_tras = pd.DataFrame({
    "customer_id" : [ 1, 2, 5, 4],
    "transaction" : [ 10, 20, 30, 40]
})

merge = pd.merge(data_object, data_tras, on="customer_id", how="inner")
conct = pd.concat([data_object, data_tras], axis= 1, ignore_index= True)
print(conct)


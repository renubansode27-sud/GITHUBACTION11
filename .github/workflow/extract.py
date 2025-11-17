import pandas as pd

print ("extract data from mysql")

data = {
    'id':[1,2,3],
    'name':['a','b','c']
}

df = pd.DataFrame(data)
print(df)
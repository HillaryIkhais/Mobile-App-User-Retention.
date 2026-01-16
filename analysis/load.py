import pandas as pd 

app_data = pd.read_csv("Mobile app data.csv")
app_data.head()
print(app_data.columns)

app_data.info()
app_data.isnull().sum()

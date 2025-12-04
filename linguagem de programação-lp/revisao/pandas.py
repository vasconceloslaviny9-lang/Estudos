import pandas as pd
df = pd.read_csv("titanic.csv")

#Ver dados
print(df.head())
print(df.info())
print(df.describe())

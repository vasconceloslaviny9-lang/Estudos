import pandas as pd

dados_df = pd.read_excel("produtos_ficticios.xlsx") 

#Qual é o produto mais caro e qual e o mais barato?

mais_caro = dados_df.loc[dados_df['Preço'].idxmax()]
print(mais_caro)

mais_barato = dados_df.loc[dados_df['Preço'].idxmin()]
print(mais_barato)
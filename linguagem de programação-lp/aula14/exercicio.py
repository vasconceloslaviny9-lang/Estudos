import pandas as pd

#Mostre o nome e preço dos produtos com valor acimas de 300 reais 

dados_df = pd.read_excel("produtos_ficticios.xlsx") 
#caros = dados_df[dados_df['Preço'] > 300][['Nome do produto', 'Preço']]
#print(caros)
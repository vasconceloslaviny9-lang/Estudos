import pandas as pd

dados_df = pd.read_excel ("produtos_ficticios.xlsx")

#liste os produtos fabricados na china com o estoque acima de 50 unidades

prod_fabr = dados_df.loc[(dados_df['País de origem'] == 'China') & (dados_df['Quantidade em estoque'] > 50), ['Nome do produto', 'País de origem', 'Quantidade em estoque']]
print(prod_fabr)
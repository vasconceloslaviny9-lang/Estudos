import pandas as pd

dados_df = pd.read_excel("produtos_ficticios.xlsx") 
# print(dados_df.to_string()) 
# print(dados_df.columns)
# print(dados_df.shape)

# produto = dados_df[['Categoria', 'Código do produto']]
# print(produto)

# roupa = dados_df.loc[dados_df['Cor'] == "Preto" , ["Cor", "Nome do produto", "Preço"]]
# print(roupa)

# produto_cor_df = dados_df.loc[(dados_df["Categoria"] == "Roupas") & (dados_df["Cor"] == "Preto"), ["Categoria" , "Código do produto" , "Preço" , "Cor"]]
# print(produto_cor_df)

print(dados_df.loc[5, 'Código do produto'])

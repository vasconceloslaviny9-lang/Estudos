"""
Vamos praticar Pandas usando o dataset Titanic.csv.
Este trabalho vale 15 pontos.

Lembre-se: o semestre está acabando e a prova está chegando.
Aprenda!!
"""

#--------------------------------------------------
# 1. Importação da biblioteca e carregamento
#--------------------------------------------------
import pandas as pd
#importe aqui a planilha

dados_df= pd.read_csv("titanic.csv")
#--------------------------------------------------
# 2. Explorando o dataset
#--------------------------------------------------

#--------------------------------------------------
# 3. Exercícios (RESPONDA USANDO CÓDIGO EM PYTHON)
#--------------------------------------------------

# 1) Quantas linhas e colunas o dataset possui?
#    Dica: use df.shape

#print("Linhas, Colunas:", dados_df.shape)



# 2) Qual é a idade média dos passageiros?
#    Dica: mean()

#mean_age = dados_df['Age'].mean()
#print(f"Idade média dos passageiros: {mean_age:.2f}")



# 3) Trazer apenas as colunas 'Name' e 'Age'

#cols_name_age =dados_df[['Name', 'Age']]
#print(cols_name_age.head())



# 4) Trazer apenas os passageiros do sexo feminino

#mulheres = dados_df[dados_df['Sex'] == 'female']
#print(mulheres.head())


# 5) Trazer apenas passageiros do sexo masculino com idade > 30

#passageiros_masculinos_acima_30 = dados_df[(dados_df['Sex'] == 'male') & (dados_df['Age'] > 30)]
#print(passageiros_masculinos_acima_30)



# 6) Mostrar apenas mulheres sobreviventes

#mulheres_sobreviventes = dados_df[(dados_df['Sex'] == 'female') & (dados_df['Survived'] == 1)]
#print(mulheres_sobreviventes)

# 7) Mostrar passageiros da 1ª classe com menos de 18 anos

#passageiros_primeira_menores = dados_df[(dados_df['Pclass'] == 1) & (dados_df['Age'] < 18)]
#print(passageiros_primeira_menores)


# 8) Criar uma coluna chamada 'Faixa' com:
#       - CRIANCA para idade < 18
#       - ADULTO para idade >= 18


#df['Faixa'] = df['Age'].apply(lambda x: 'Criança' if x < 18 else 'Adulto')
#print(df[['Name' , 'Age', 'Faixa']])


# 9) Agrupar e mostrar taxa de sobrevivência por sexo



#print(df.groupby('Sex')['Survived'].mean())


# 10) Mostrar a tarifa média por classe


#print(df.groupby('Pclass')['Fare']. mean())


# 11) Qual é a idade da pessoa mais velha do Titanic?
#     Dica: df['Age'].max()


#print(df['Age'].max())

# 12) Qual foi a tarifa mais alta paga no Titanic?
#     Dica: df['Fare'].max()


#print(df['Fare'].max())


# 13) Qual classe tinha mais passageiros?
#     Dica: use value_counts()


#print(df['Pclass'].value_counts())

#--------------------------------------------------
# 5. Exportação
#--------------------------------------------------

# 14) Exportar apenas os sobreviventes para um arquivo CSV
#     Nome sugerido: sobreviventes.csv

#sobreviventes = df[df['Survived']==1]
#sobreviventes.to_csv('sobreviventes.csv', index=False)


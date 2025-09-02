pessoa = {
    "nome" : "Laviny",
    "idade" : 17,
    "peso" : 54
    
}
print(pessoa) #Mostra todos atributos(nome, idade, peso)
print(pessoa["nome"]) #mostra so a casa q que mostrar
print(pessoa.keys())#Mostra somente os atributos
print(pessoa.values())#Mostra somente os valores
pessoa["altura"] = 1.65 #Acrescentar ou modificar algum atributo (Adicionar ou retirar)
print(pessoa)

pessoa["peso"] = 50
print(pessoa)

del pessoa["idade"] #Remover algum atributo
print(pessoa)

print("nome" in pessoa )
print ("idade" in pessoa)


with open("dados.txt" , "w") as arquivo:
    arquivo.write("Laviny")

with open("dados.txt", "r") as arquivo:
    conteudo = arquivo.read()
print(conteudo)    

with open("dados.txt", "a") as arquivo:
    arquivo.write("\n Vasconcelos")

#

nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")

with open("aula.txt", "w") as arquivo:
    arquivo.write( f"\n nome: {nome} ")
    arquivo.write( f"\n idade: {idade} ")

    print("Dados gravas com sucesso no arquivo aula09.txt")

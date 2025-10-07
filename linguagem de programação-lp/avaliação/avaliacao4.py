nome1 = str(input("Digite um nome: " ))
nome2 = str(input("Digite outro nome: " ))
nome3 = str(input("Digite outro nome: " ))


with open("aluno.txt" , "w") as arquivo:
    arquivo.write(f"{nome1} \n")
    arquivo.write(f"{nome2} \n")
    arquivo.write(f"{nome3} \n")

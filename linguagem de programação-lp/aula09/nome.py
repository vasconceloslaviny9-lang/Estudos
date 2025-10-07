n = input("Qual é seu nome? ")
i = input("Qual sua idade? ")

with open ("aula09.txt", "w") as arquivo:
    arquivo.write(n)
    arquivo.write(f"\n{i}")
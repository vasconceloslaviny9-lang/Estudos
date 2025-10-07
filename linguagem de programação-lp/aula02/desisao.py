valor = int(input("Qual a sua idade?"))
if valor > 18: 
    print("você pode dirigir")
else:
    print("Você não pode dirigir")

 #exercicio
 
nota_1 = float(input("qual foi sua nota_1?"))
nota_2 = float(input("qual foi sua nota_2?"))
media = (nota_1 + nota_2) / 2
print("Média=", media)
if media > 6:
    print("Você foi aprovado")
elif media > 4 and media <=5:
    print("Recuperação")
else:
    print("Você foi reprovado")

#if=se  elif=senao 
#float=real  int=inteiro  string=texto  bool=v ou f
try:
    a = int(input("Digite um número inteiro: "))

except ValueError:
    print("Entrada invalida, tente novamente")
else:
    print("Número válido")

finally:
    print("Seu programa foi execultado")

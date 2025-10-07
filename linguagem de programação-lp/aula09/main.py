try:
    a = int(input("Numerador:"))
    b = int(input("Denominador:")) 

    d = a/b



except ZeroDivisionError:
    print("Nao é possivel dividir por zero")

except ValueError:
    print("Você digitou um valor inválido")

else:
    print(f"O resultado é: {d}")

finally:
    print("Seu programa foi execultado")


#try = operação
#except = falhou
#else = deu certo
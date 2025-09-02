import operacoes

print("==calculadora")
print("1- somar")
print("2- subtrair")
print("3- multiplicar")
print("4- dividir")

opcao = int(input("Escolha a operação"))
a = float(input("Digite o primeiro número:"))
b = float(input("Digite o segundo número:"))

if opcao == 1:
    print("Resultado:", operacoes.soma(a,b))

elif opcao == 2:
    print("Resultado:", operacoes.sub(a,b))
 
elif opcao == 3:
    print("Resultado:", operacoes.mult(a,b))

elif opcao == 4:
    print("Resultado:", operacoes.dividir(a,b))

else:
    print("opção invalida")





import operacoes
print("Qual conversão voce deseja utilizar?")
print("1- metros para centimetros")
print("2- centimetros para metros")
print("3- km para metros")


opcao = int(input("Escolha a conversão"))
a = float(input("Digite o primeiro número:"))


if opcao == 1:
    print("Resultado:", operacoes.metros_para_centimetros(a))

elif opcao == 2:
    print("Resultado:", operacoes.centimetros_para_metros(a))
 
elif opcao == 3:
    print("Resultado:", operacoes.km_para_metros(a))

else:
    print("opção invalida")



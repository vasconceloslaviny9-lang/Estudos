x = int (input("Digite o valor para x: "))
print(x)
y = int (input("Digite o valor para y: "))
print(y)
z = (x**2+y**2)/(x+y)**2
print("z=",z)


#Exemplol prático para usar MOD.
total_meses = 170
ano = total_meses // 12
meses = total_meses % 12
print("O consorcio é de", ano, "anos é", meses, "meses")
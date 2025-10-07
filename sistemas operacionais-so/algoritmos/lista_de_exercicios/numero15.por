programa {

  inteiro dias, horas_mes
  real salario


  funcao inicio() {

   escreva("Digite o número de dias trabalhados no mês: ")
   leia(dias)
   
   horas_mes = dias * 8
   salario = horas_mes * 25
   
   escreva("O funcionário trabalhou ", horas_mes, " horas no mês.")
   escreva("\nO salário do funcionário é: R$ ", salario)




    
  }
}

programa {
  real salario_funcionario, novo_salario, aumento_salario
  funcao inicio() {
    escreva("Qual é o seu salário? ")
    leia(salario_funcionario)

    aumento_salario = salario_funcionario*0.15
    novo_salario = salario_funcionario + aumento_salario
    escreva("O aumento do novo salário é de ",aumento_salario)
    escreva("\nO novo sera de ", novo_salario)

    
  }
}

programa {

  inteiro numero_1, numero_2
  logico e_multiplo

  funcao inicio() {
    escreva("Digite o primeiro número inteiro: ")
      leia(numero_1)
    escreva("Digite o segundo número inteiro: ")
      leia(numero_2)
    se (numero_2 == 0)
    escreva("O segundo número não pode ser zero.")
    senao
    e_multiplo = (numero_1 % numero_2 == 0)
     escreva("O primeiro número é múltiplo do segundo? ", e_multiplo)



 

    
  }
}

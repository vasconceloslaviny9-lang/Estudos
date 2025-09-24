programa {
  real valor_1, valor_2, valor_3
  real soma_total, media
  funcao inicio() {
    escreva("Digite o primeiro valor:")
    leia(valor_1)
    escreva("Digite o segundo valor:")
    leia(valor_2)
    escreva("Digite o terceiro valor:")
    leia(valor_3)

    soma_total = valor_1 + valor_2 + valor_3
    media = (valor_1 + valor_2 + valor_3) / 3

    escreva("--- Resultados ---\n",
            "Valores:", valor_1 ,", ",  valor_2, ", ", valor_3,"\n",
            "soma_total:" , soma_total,"\n",
            "Média:", media

      



          )
    
  }
}

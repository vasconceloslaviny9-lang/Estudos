programa {
   real preco1, preco2
  logico preco_menor, precos_iguais

  funcao inicio() {
    
  escreva("Digite o preço do primeiro produto: ")
  leia(preco1)

  escreva("Digite o preço do segundo produto: ")
  leia(preco2)

  preco_menor = (preco1 < preco2)
  precos_iguais = (preco1 == preco2)

  escreva("O preço do primeiro produto é menor que o do segundo? ", preco_menor)
  escreva("\nOs preços dos dois produtos são iguais? ", precos_iguais)

    
  }
}

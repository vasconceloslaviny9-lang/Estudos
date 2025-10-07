programa {
  real valor_produto, preco_promocional, preco_final
  funcao inicio() {
    
    escreva("Qual é o valor do produto? ")
    leia(valor_produto)

    preco_promocional = valor_produto*0.05
    preco_final = valor_produto-preco_promocional

    escreva("O valor do desconto é de ", preco_promocional)
    escreva("\nO valor final é de ", preco_final)

    
  }
}

programa {
  const real desconto_porcentagem = 0.15
  cadeia produto
  real preco, desconto, preco_com_desconto

  funcao inicio() {
    escreva("Nome do Produto:")
    leia(produto)
    escreva("Preço original:")
    leia(preco)

    desconto = preco * desconto_porcentagem
    preco_com_desconto = preco - desconto
    
    escreva("--- Preço Promocional ---\n",
            "Produto:", produto, "\n",
            "Preço Original:", preco, "\n",
            "Desconto (15.0%):", desconto, "\n",
            "Preço Final: ", preco_com_desconto
                       
          )
  }
}

programa {
  funcao inicio() {
    
    const real percentual_desconto= 0.10
    
    
    cadeia nome_cliente
    real valor_total_produtos
    cadeia forma_pagamento
    real valor_desconto
    real valor_final_compra
    logico ganhou_brinde
    
    
    escreva("--- Sistema de Caixa da Loja ---\n")
    escreva("Nome do Cliente: ")
    leia(nome_cliente)
    escreva("Valor total dos produtos: R$ ")
    leia(valor_total_produtos)
    escreva("Forma de pagamento (PIX ou Cartão): ")
    leia(forma_pagamento)
    
    
    valor_desconto = valor_total_produtos * percentual_desconto
    
    
    valor_final_compra = valor_total_produtos - valor_desconto
    
    
    ganhou_brinde = (valor_final_compra > 100.0) e (forma_pagamento == "PIX")
    
    
    escreva("\n--- Recibo para ", nome_cliente, " ---\n")
    escreva("Valor dos Produtos: R$ ", valor_total_produtos, "\n")
    escreva("Desconto (10%): R$ ", valor_desconto, "\n")
    escreva("Valor Final da Compra: R$ ", valor_final_compra, "\n")
    escreva("Forma de Pagamento: ", forma_pagamento, "\n")
    escreva("Cliente ganhou brinde especial? ", ganhou_brinde, "\n")
  }
}
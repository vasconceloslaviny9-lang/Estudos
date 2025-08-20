programa {
  cadeia nome_1, nome_2
  inteiro quantidade_1, quantidade_2
  real preco1, preco2, subtotal1, subtotal2, total

  funcao inicio() {

    escreva("--- Supermercado Preço Bom ---\n")
    escreva("Vamos registrar sua compra!\n")
    
    // Produto 1
    escreva("--- PRODUTO 1 ---\n")
    escreva("Digite o nome do produto: ", nome_1)
    leia(nome_1)
    escreva("Digite a quantidade: ", quantidade_1)
    leia(quantidade_1)
    escreva("Digite o preço unitário (ex: 5.50) :", preco1)
    leia(preco1)

   //-------------------------------------------------------//
   // Produto 2
    escreva("\n--- PRODUTO 2 ---\n")
    escreva("Digite o nome do produto: ", nome_2)
    leia(nome_2)
    escreva("Digite a quantidade: ", quantidade_2)
    leia(quantidade_2)
    escreva("Digite o preço unitário (ex: 8.99): ", preco2)
    leia(preco2)

    // Cálculos
    subtotal1 = quantidade_1 * preco1
    subtotal2 = quantidade_2 * preco2
    total = subtotal1 + subtotal2

    // Recibo
    escreva("-- RECIBO DA COMPRA ---\n")
    escreva("Item: ", nome_1, "\n")
    escreva("Quantidade: ", quantidade_1, "| Preço unit: ", preco1, "| subtotal:", subtotal1)
    escreva("Quantidade: ", quantidade_2, "| Preço unit: ", preco2, "| subtotal:", subtotal2)
    escreva("\n")
    escreva("-----------------------------------------------------\n")
    total = subtotal1 + subtotal2
    escreva("VALOR TOTAL DA COMPRA: R$", total)
    escreva("\n")
    escreva("------------------------------------------------------")
  }
}

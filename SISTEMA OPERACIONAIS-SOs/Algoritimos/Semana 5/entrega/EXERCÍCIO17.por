programa {
  cadeia nome_do_item
  real peso_unitario
  inteiro quantidade_em_posse
  real peso_total
  funcao inicio() {
    escreva("Nome do item: ")
    leia(nome_do_item)
    escreva("Peso unitário (Oz): ")
    leia(peso_unitario)
    escreva("Quantidade em posse:")
    leia(quantidade_em_posse)
    peso_total = peso_unitario * quantidade_em_posse
    escreva("--- Detalhe do Item ---\n")
    escreva("Item: ", nome_do_item, "\n")
    escreva("Quantidade:", quantidade_em_posse, "\n")
    escreva("Peso Unitário: ", peso_unitario, " Oz" , "\n")
    escreva("Peso Total: ", peso_total)
    
  }
}

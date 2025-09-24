programa {

  const cadeia nome_magia = "Energy Beam"
  const inteiro custo_mana_magia = 20
  inteiro quantidade_lancamento
  inteiro custo_total_mana

  funcao inicio() {
    
escreva("--- Calculadora de Custo de Mana (Magia: ", nome_magia, ") ---\n")

escreva("Quantas vezes você pretende lançar a magia '", nome_magia, "'? ")
leia(quantidade_lancamento)

custo_total_mana = quantidade_lancamento * custo_mana_magia

escreva("\nPara lançar a magia '", nome_magia, "' ", quantidade_lancamento, " vez(es), você gastará: ", custo_total_mana, " de mana.\n")
    }


    
  }
}

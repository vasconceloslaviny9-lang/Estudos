programa {
  real preco_litro_combustivel, consumo_do_carro, distancia, custo_total_viagem
  funcao inicio() {
    escreva("Preço do combustível(R$/L): ")
    leia(preco_litro_combustivel)
    escreva("Consumo do carro (Km/L): ")
    leia(consumo_do_carro)
    escreva("Distância da viagem (Km): ")
    leia(distancia)
    custo_total_viagem = (distancia / consumo_do_carro) * preco_litro_combustivel
    escreva(" O custo total da viagem será de R$ ", custo_total_viagem)

  }
}

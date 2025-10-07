programa {
  real largura, altura,area_a_ser_pintada, quantidade_de_tinta
  funcao inicio() {
    escreva("Qual é a largura da parede? ")
    leia(largura)
    escreva("Qual é a altura da parede? ")
    leia(altura)
    area_a_ser_pintada= largura*altura
    escreva("A area a ser pintada é de ", area_a_ser_pintada, "M\n")

    quantidade_de_tinta = area_a_ser_pintada/2
    escreva("A quantidade de tinta necessária e de ", quantidade_de_tinta, " L ")


    
  }
}

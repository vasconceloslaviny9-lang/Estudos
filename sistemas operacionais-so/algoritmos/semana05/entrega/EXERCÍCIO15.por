programa {
  real peso, altura, imc
  funcao inicio() {
    escreva("Digite seu peso (Kg): ")
    leia(peso)
    escreva("Digite sua altura (m): ")
    leia(altura)
    imc = peso / (altura * altura)
    escreva("Seu IMC é :", imc)
    
  }
}

programa
{
funcao inicio(){
real velocidade, multa
inteiro km_acima

escreva("Digite a velocidade do carro (em Km/h): ")
leia(velocidade)

se (velocidade > 80){
km_acima = velocidade - 80
multa = km_acima * 5

escreva("Você foi multado por excesso de velocidade!\n")
escreva("Velocidade acima do permitido: ", km_acima, " Km/h\n")
escreva("Valor da multa: R$", multa, "\n")
 }
senao {
escreva("Velocidade dentro do limite. Dirija com segurança!\n")
}
}
}
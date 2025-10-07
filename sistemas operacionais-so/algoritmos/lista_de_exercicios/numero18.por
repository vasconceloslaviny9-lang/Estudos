programa
{
funcao inicio(){

inteiro ano_nascimento, ano_atual, idade

escreva("Digite o ano de nascimento: ")
leia(ano_nascimento)

escreva("Digite o ano atual: ")
leia(ano_atual)

idade = ano_atual - ano_nascimento

escreva("Você tem ", idade, " anos.\n")

se (idade >= 16) {
escreva("Você pode votar.")}

senao{

escreva("Você não pode votar.")}
}

}
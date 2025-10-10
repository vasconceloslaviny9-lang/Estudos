programa {
  real nota_1, nota_2, media
  cadeia nome
  funcao inicio() {
    escreva("Digite o nome do aluno: ")
    leia(nome)

    escreva("Digite sua primeira nota: ")
    leia(nota_1)
    escreva("Digite sua segunda nota: ")
    leia(nota_2)
    media = (nota_1 + nota_2) / 2
    escreva("A média do aluno ", nome , " é ", media, "\n")

    se (media>= 7){
      escreva("\nO aluno teve um bom aproveitamento!")
    }
    senao{
      escreva("\nO aluno não teve um bom aproveitamento")
    }
    
    
  }
}

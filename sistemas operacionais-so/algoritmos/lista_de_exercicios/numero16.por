programa {
  inteiro  cigarros_dia, anos, total_cigarros
  real minutos_perdidos, dias_perdidos
  funcao inicio() {

  escreva("Digite a quantidade de cigarros fumados por dia: ")
  leia(cigarros_dia)

  escreva("Digite há quantos anos você fuma: ")
  leia(anos)

  total_cigarros = cigarros_dia * 365 * anos
  minutos_perdidos = total_cigarros * 10
  dias_perdidos = minutos_perdidos / (24 * 60)

     
  escreva("Total de cigarros fumados: ", total_cigarros)
  escreva("\nO fumante perdeu aproximadamente ", dias_perdidos, " dias de vida")




    
  }
}

programa { 
  real celsius, fahrenheit

  funcao inicio() {
    escreva("Digite a temperatura em Celsius:")
    leia(celsius)
    escreva("Temperatura em Celsius:", celsius, "°C" ,"\n")
    fahrenheit = (celsius * 9.0/5.0) + 32
    escreva("Temperatura em Fahrenheit:", fahrenheit, " F")
    
    
  }
}

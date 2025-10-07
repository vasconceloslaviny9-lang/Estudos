programa {
  real distancia, km, hm, dam, dm, cm, mm
  funcao inicio() {

    escreva("Digite uma distância em metros: ")
    leia(distancia)
    
    km= distancia/1000
    hm= distancia/100
    dam= distancia/10
    dm= distancia*10
    cm=distancia*100
    mm=distancia*1000

    escreva("A distância de " , distancia,"m corresponde a:\n", km, "Km\n" ,hm,"Hm\n", dam,"Dam\n", dm,"Dm\n", cm,"Cm\n", mm, "Mm\n")

    
  }
}

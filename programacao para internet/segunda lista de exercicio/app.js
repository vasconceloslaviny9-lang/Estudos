function ex001() {
  let texto = document.querySelector("h1");
  texto.textContent = "Hora do Desafio";

}
function ex002() {
  console.log("O botão foi clicado");

}
function ex003() {
  alert("Eu amo JS");

}
function ex004() {
  let cidade = prompt("Fale uma cidade do Brasil");
  alert("Estive em " + cidade + " e lembrei de você");

}
function ex005() {
  let numero1 = parseInt(prompt("Digete um número"));
  let numero2 = parseInt(prompt("Digete outro número"));
  let soma = numero1 + numero2;
  alert(soma);

}
function ex006() {
  console.log("Olá Mundo");

}
function ex007() {
  let nome = document.getElementById("inputEx07").value
  console.log("Olá " + nome + "!");

}
function ex008() {
  let numero = parseInt(document.getElementById("inputEx008").value)
  let resultado = numero * 2;
  let campoResultado = document.getElementById("resultadoEx008");
  campoResultado.textContent = resultado


}
function ex009() {
  let numero1 = parseInt(document.getElementById("inputEx009").value)
  let numero2 = parseInt(document.getElementById("inputEx009").value)
  let numero3 = parseInt(document.getElementById("inputEx009").value)

  let media = (numero1 + numero2 + numero3) / 3;
  let resultado = document.getElementById("resultadoEx009");
  resultado.textContent = media;
}
function ex010() {
  let numero1 = parseInt(document.getElementById("inputNumero4").value);
  let numero2 = parseInt(document.getElementById("inputNumero5").value);
  let resultado = document.getElementById("resultadoEx010");
  if (numero1 > numero2) {
    resultado.textContent = numero1;
  } else {
    resultado.textContent = numero2;
  }
}
function ex011() {
  let numero = document.getElementById("inputEx011").value;
  let resultado = document.getElementById("resultadoEx011");
  let multiplicacao = (numero * numero);
  resultado.textContent = multiplicacao;
}
function ex012() {
  let peso = parseFloat(document.getElementById("inputEx012").value);
  let altura = parseFloat(document.getElementById("inputEx0012").value);
  let resultado = document.getElementById("resultadoEx012");
  let imc = peso / (altura * altura);
  resultado.textContent = imc;

}
function ex013() {
  let numero = document.getElementById("inputEx013").value;
  let resultado = document.getElementById("resultadoEx013");
  let fatorial = 1
  for (let i = numero; i >= 1; i--) {
    fatorial = fatorial * i;
  }
  resultado.textContent = fatorial;

}
function ex014(){
  let numero = document.getElementById("inputEx014").value;
  let resultado = document.getElementById("resultadoEx014");
  let converte = numero * 4.8;
  resultado.textContent = `R$ ${converte}`;
}
function ex015(){
  let altura = parseFloat(document.getElementById("input15").value);
  let largura = parseFloat(document.getElementById("input16").value);
  let calculo1  = altura * largura;
  let calculo2 = (altura * 2) + (largura * 2);
  let resultado1 = document.getElementById("resultado1")
  let resultad02 = document.getElementById("resultado2")
  resultado1.textContent = calculo1;
  resultad02.textContent = calculo2;
}
function ex016(){

}
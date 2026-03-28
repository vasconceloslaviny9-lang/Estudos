//let titulo = document.querySelector("h1");
//titulo.innerHTML = "Jogo do Número Secreto";

//let paragrafo = document.querySelector("p");
//paragrafo.innerHTML = "Escolha um número entre 1 e 10";

function exibeMensagemInicial(tag, texto){
    let campo = document.querySelector(tag);
    campo.innerHTML = texto;
}
let tentativa = 1;

function msgInicio(){
exibeMensagemInicial("h1", "Jogo do Número Secreto")
exibeMensagemInicial("p", "Escolha um número entre 1 e 10")
}

msgInicio()

numeroSecreto = gerarNumeroSecreto();


function gerarNumeroSecreto(){
    return parseInt(Math.random() * 10 +1);

}


function verificarChute(){
    let chute = document.querySelector("input").value;

    if (chute == numeroSecreto){
        exibeMensagemInicial("h1", "Acertou")

        let palavrasTentativa = tentativa == 1? "tentativa":"tentativas";
        let msgTentativa = `Você acertou o número secreto  (${numeroSecreto}), com ${tentativa} ${palavrasTentativa}`
    
        exibeMensagemInicial("p", msgTentativa )

        document.getElementById("reiniciar").removeAttribute("disabled");
        
    }
    else{
        tentativa++;

        if (chute > numeroSecreto){
            exibeMensagemInicial("p", "O número secreto é Menor");
        }

        else{
                exibeMensagemInicial ("p", " O número secreto é Maior")
            }
            limparCampo()
        }
    }
    function limparCampo() {
        chute = document.querySelector("input");
        chute.value = "";
        
    }
    function novoJogo(){
        msgInicio();
        numeroSecreto = gerarNumeroSecreto();
        tentativa = 1;
        limparCampo();
        document.getElementById("reiniciar").setAttribute("disabled", true);
    }

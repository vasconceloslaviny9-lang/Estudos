function sortear() {

    let quantidade = parseInt(document.getElementById ("quantidade").value);
    let de = parseInt(document.getElementById ("de").value);
    let ate = parseInt(document.getElementById ("ate").value);

    // If e Else para impedir com que o site Crash
    if (de > ate){
        alert("Aí c me quebra chefe, isso aí num dá!")
    }
    else if ((ate+1) - de >= quantidade){

        //console.log(quantidade);
        //console.log(de);
        //console.log(ate);

        let numero;
        let sorteados = [];

    for (let i = 0; i < quantidade; i++){
        numero = gerarNumeroAleatorio(de, ate);
        

        //enquanto número não estiver na lista
        while (sorteados.includes(numero)){
            numero = gerarNumeroAleatorio(de, ate);
        }

        sorteados.push(numero);
    }

    let resultado = document.getElementById("resultado");
    resultado.innerHTML = `<label class="texto__paragrafo">Números sorteados:  ${sorteados} </label>`

    alterarStatusBotao()

    }

    else {
        alert("Vai tomar no c#")
    }
}

    function reiniciarJogo(){
    document.getElementById ("quantidade").value = "";
    document.getElementById ("de").value = "";
    document.getElementById ("ate").value = "";
    document.getElementById ("resultado").innerHTML = '<label class="texto__paragrafo">Números sorteados:  nenhum até agora</label>'
    alterarStatusBotao()
    }


function alterarStatusBotao(){
    let botao = document.getElementById("btn-reiniciar")
    if (botao.classList.contains("container__botao-desabilitado")){
        botao.classList.remove("container__botao-desabilitado")
        botao.classList.add("container__botao")

    }
    else {
        botao.classList.add("container__botao-desabilitado")
        botao.classList.remove("container__botao")
    }
}



function gerarNumeroAleatorio(min, max){
    return Math.floor(Math.random() * (max - min + 1)) + min;
}
        
    
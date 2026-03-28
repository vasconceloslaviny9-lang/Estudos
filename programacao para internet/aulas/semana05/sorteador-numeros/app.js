function sortear(){

    let quantidade = parseInt (document.getElementById('quantidade').value);
    let de = parseInt (document.getElementById('de').value);
    let ate =parseInt ( document.getElementById('ate').value);

    let numero ;
    let sorteados = [];

    for(let i = 0; i < quantidade; i++){
        numero = gerarNumeroAleatorio(de, ate);

        while (sorteados.includes(numero)){
            numero = gerarNumeroAleatorio(de, ate)
        }
        sorteados.push(numero);
    }

    let resultado = document.getElementById('resultado');
    resultado.innerHTML = `<label class="texto__paragrafo">Números sorteados:  ${sorteados}</label>`
    alterarStatusbotao();

    function reiniciarJogo(){
        document.getElementById('quantiadade').value = '';
        document.getElementById('de').value ='';
        document.getElementById('ate').value = '';
        document.getElementById('resultado').innerHTML = '<label class="texto_paragrafo">Número sorteados:nenhum até agora</label>';
        alterarStatusbotao();
    }

function alterarStatusbotao(){
    let botao = document.getElementById('btn-reiniciar');
    
    if (botao.classList.contains('container_botao-desabilitado')){
        botao.classList.remove('container_botao-desabilitado');
        botao.classList.add('container_botao')
    }
    else{
        botao.classList.add('container_botao-desabilitado');
        botao.classList.remove('container_botao')
    }
}


function gerarNumeroAleatorio(min, max){
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

}


//console.log(quantidade);
//console.log(de);
//console.log(ate);

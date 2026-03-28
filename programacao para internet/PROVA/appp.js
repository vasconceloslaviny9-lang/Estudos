function comprar(){

let tipo = document.getElementById("tipo-ingresso").value;
let qtd = parseInt(document.getElementById("qtd").value);

if (tipo == "pista"){
    comprar_pista(qtd);
}else if (tipo == "superior"){
    comprar_superior (qtd);
}else{
    comprar_inferior (qtd);
}

}
function comprar_pista(qtd){
    let qtd_pista = parseInt(document.getElementById("qtd-pista").textContent);
    if (qtd < qtd_pista){
        let conta = qtd_pista - qtd;
        document.getElementById("qtd-pista").textContent = conta 
    } else {
        alert ("Não é possivel")
    }
}

function comprar_superior(qtd){
    let qtd_superior = document.getElementById("qtd-superior").textContent;
    if (qtd < qtd_superior){
        let conta = qtd_superior - qtd;
        document.getElementById("qtd-superior").textContent = conta 
    } else {
        alert ("Não é possivel")
    }
}

function comprar_inferior(qtd){
    let qtd_inferior = document.getElementById("qtd-inferior").textContent;
    if (qtd < qtd_inferior){
        let conta = qtd_inferior - qtd;
        document.getElementById("qtd-inferior").textContent = conta 
    } else {
        alert ("Não é possivel")
    }
}



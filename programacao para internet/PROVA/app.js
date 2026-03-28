function alterarStatus(id) {
   
let jogo = document.getElementById (`game-${id}`);
let img = jogo.querySelector(".dashboard__item__img");
let botao = jogo.querySelector(".dashboard__item__button");


if(botao.classList.contains("dashboard__item__button--return")){

    botao.classList.remove("dashboard__item__button--return")
    botao.innerHTML = "Alugar"
    img.classList.remove("dashboard__item__img--rented")
   
}
else{

    botao.classList.add("dashboard__item__button--return")
    botao.innerHTML = "Devolver"
    img.classList.add("dashboard__item__img--rented")
}



}
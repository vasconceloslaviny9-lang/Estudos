let total = 0;
let carrinho;

function adicionar(){

    let produto = document.getElementById('produto').value;
    let quantidade = document.getElementById('quantidade').value;

    let val_und = produto.split('R$')[1];
    let nom_prdt = produto.split('-')[0];
    
    let val_parcial = (val_und * quantidade);

    //carrinho
    let carrinho = document.getElementById('lista-produtos')
    carrinho.innerHTML = carrinho.innerHTML + `
    <section class="carrinho__produtos__produto">
        <span class="texto-azul">${quantidade}x </span> ${nom_prdt} <span class="texto-azul"> R$${val_parcial}</span>
    </section>
    `;

    total = total + val_parcial;
    let campoTotal = document.getElementById("valor-total");
    campoTotal.innerHTML = `R$ ${total}`;

    document.getElementById("quantidade").value = "";

}

function limpar(){

    let carrinho = document.getElementById('lista-produtos')
    carrinho.innerHTML = ``;
    
    let campoTotal = document.getElementById("valor-total");
    campoTotal.innerHTML = 'R$';

}
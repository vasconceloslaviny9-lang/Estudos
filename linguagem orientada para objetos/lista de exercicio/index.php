<?php

$numero = $argv[1];
$nomeDaFuncao = 'ex' . $numero;

echo "========================================\n";
echo "   Executando o Exercício $numero\n";
echo "========================================\n\n";

$nomeDaFuncao(); 

echo "\n========================================\n";


// ÁREA DOS EXERCÍCIOS: Funções com a lógica de cada questão
// ==============================================================================

function ex1() {
    echo "Olá, Mundo!\n";
}

function ex2() {
    $nome = readline("Qual é o seu nome? ");
    echo "Olá $nome, é um prazer te conhecer!\n";
}

function ex3(){
    $nome = readline("Nome do Funcionario:");
    $salario = floatval(readline("Salário:"));
    echo "O funcionario $nome tem um salário de $salario em Junho";
}

function ex4(){
    $valor1 = readline("Digite um valor:");
    $valor2 = readline("Digite outro valor:");
    $soma = $valor1 + $valor2;
    echo "A soma entre $valor1 e $valor2 é igual a $soma ";

}

function ex5(){
    $nota1 = readline("Digite um valor:");
    $nota2 = readline("Digite outro valor:");
    $media = ($nota1 + $nota2) / 2;
    echo "A média entre $nota1 e $nota2 é igual a $media ";    
}

function ex6(){
    $numero = readline("Digite um numero:");
    $antecessor = $numero - 1;
    $sucessor = $numero + 1;
    echo "O antecesso de $numero é: $antecessor \n";
    echo "O sucessor de $numero é: $sucessor ";

}
function ex7(){
    $numero = readline("Digite em número")
}
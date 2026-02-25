<?php


 $nomeFilme = "[=´=-0Top Gun - Maverick"; //string

 $anoLancamento = $argv[1] ?? 2022; //2022; //Int
 $incluidoNoPlano = true; //Bool

 $genero = match ($nomeFilme) {
    "Top Gun - Maverick" => "Ação",
    "Thor ragnarok" => "herói",
    "Se beber não case" => "Comedia",
     default => "Desconhecido",

 };

 $somaDeNotas +=9;
 $somaDeNotas += 6;
 $somaDeNotas +=8;
 $somaDeNotas += 7.5;
 $somaDeNotas += 5;

 $notaDeFilme = $somaDeNotas/5;

 $planoprime = true;
 $incluidoNoPlano = $planoprime || $anoLancamento < 2000;

 

    echo "\n Bem Vindo ao Screen Match
    ";
    echo "Nome do  Filme:$nomeFilme"; //interpolação aspas duplas
    
    echo '
    Ano de Lançamento:'.$anoLancamento; //concatenação]

    echo "
    Nota do Filme:$notaDeFilme";
    echo "
    Incluido no Plano: $incluidoNoPlano \n";
    echo "
    Genero do filme: $genero \n";


    if ($anoLancamento > 2022){
    echo 'Lançamento!';}
elseif ($anoLancamento > 2020 && $anoLancamento <= 2022){
    echo 'Ainda é novo.';}
else{
    echo 'Não é lançamento.';
 }
<?php


 $nomeFilme = "Top Gun - Maverick"; //string

 $anoLancamento = 2022; //Int
 $incluidoNoPlano = true; //Bool

 $genero = match ($nomeFilme) {
    "Top Gun - Maverick" => "Ação",
    "Thor ragnarok" => "herói",
    "Se beber não case" => "Comedia",
    default => "Desconhecido",

 };
 $qtddeDeNotas = ($argc - 1);

 $notas = [];

 for ($contador = 1; $contador  < $argc; $contador ++) {
    $notas[] = (float) $argv [$contador ];
 };

 //para cada indice em $notas, você da o nome de $nota, depois $somaDeNotas vai ser incrementado

$somaDeNotas = 0;
 foreach ($notas as $nota){
   $somaDeNotas += $nota;
 }

 $notaDeFilme = array_sum($notas) / $qtddeDeNotas;

 $planoprime = true;
 $incluirNoPlano = $planoprime || $anoLancamento <= 2000;
 

$notaDeFilme = $somaDeNotas/5;

 $somaDeNotas +=9;
 $somaDeNotas += 6;
 $somaDeNotas +=8;
 $somaDeNotas += 7.5;
 $somaDeNotas += 5;

 

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
    genero do filme: $genero \n";


    if ($anoLancamento > 2022){
    echo 'Lançamento!';}
elseif ($anoLancamento > 2020 && $anoLancamento <= 2022){
    echo 'Ainda é novo.';}
else{
    echo 'Não é lançamento.';
 }



$filme = [
    'nome' => "Thor: Ragnarok", 
    'ano' => 2021, 
    'nota' => 7.1, 
    'genero' => "Super Herói"];

var_dump($notas);
echo $argc;


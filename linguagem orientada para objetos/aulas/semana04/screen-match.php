<?php

echo "\nBem-vindo ao Screen Match!\n";

$nomeFilme = "Thor Ragnarok";
$anoLancamento = 2022;

$genero = match ($nomeFilme) {
    "Top Gun - Maverick" => "Ação",
    "Thor Ragnarok" => "Super Herói",
    "Se Beber não Case" => "Comédia",
    default => "Desconhecido",    
};

$qtddeNotas = ($argc-1) == 0 ? 1: ($argc-1);

$notas = [];
for ($contador = 1; $contador < $argc; $contador++) {   
    $notas[] = (float) $argv[$contador];
};

$notaFilme = array_sum($notas) / $qtddeNotas;

$planoPrime = true;

$incluidoNoPlano = $planoPrime || $anoLancamento <= 2000;

echo "Nome do Filme: " . $nomeFilme . "\n"; 
echo "Nota do Filme: $notaFilme\n";
echo "Ano de Lançamento: $anoLancamento\n";
echo "Incluido no Plano: $incluidoNoPlano\n";

//Bloco de Código
if ($anoLancamento > 2022) {
    echo "O Filme é lançamento!\n";
    }   
elseif ($anoLancamento > 2020 && $anoLancamento <= 2022){
    echo "o Filme ainda é novo\n";
    }
else {
    echo "O Filme não é um lançamento\n";
}

echo "Genero do Filme: $genero \n";

$filme = [
    'nome' => "Thor: Ragnarok",
    'ano' => 2021,
    'nota' => 7.1,
    'genero' => "Super Herói"];

echo $filme['ano'] . "\n\n";
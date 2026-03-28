<?php

require __DIR__ . "/funcoes.php";

echo "\nBem-vindo ao Screen Match!\n";

$nomeFilme = "Thor Ragnarok";
$anoLancamento = 2022;

$genero = match ($nomeFilme) {
    "Top Gun - Maverick" => "Ação",
    "Thor Ragnarok" => "Super Herói",
    "Se Beber não Case" => "Comédia",
    default => "Desconhecido",    
};

$quantidadeDeNotas = ($argc - 1) == 0 ? 1 : ($argc - 1); // Evita divisão por zero com o operado ternário

$notas =[];
for ($i = 1; $i < $argc; $i++){
    $notas[] = (float) $argv[$i];
}

$notaFilme = array_sum($notas) / $quantidadeDeNotas;

$planoPrime = true;

$incluidoNoPlano = incluidoNoPlano($planoPrime, $anoLancamento);

echo "Nome do Filme: " . $nomeFilme . "\n"; 
echo "Nota do Filme: $notaFilme\n";
echo "Ano de Lançamento: $anoLancamento\n";
echo "Incluido no Plano: $incluidoNoPlano\n";

exibeMensagemLancamento($anoLancamento);

echo "Genero do Filme: $genero\n";

$filme = [

    "nome" => "Thor: Ragnarok",
    "anolancamento" => "2021",
    "nota" => "7.5",
    "genero" => "Super-Herói"

];

echo $filme['genero'] . "\n\n";

//var_dump($notas);
//sort($notas);
//var_dump($notas);
//$menorNota = min($notas);
//echo $menorNota;

//var_dump($filme['nome']);
//$posicaoDoisPontos = strpos($filme['nome'],':'); //os dois pontos estão na posicao 4
//var_dump($posicaoDoisPontos);
//var_dump(substr($filme['nome'], 0, $posicaoDoisPontos));

echo json_encode($filme);

$filme = criarFilme(
    ano: 2021,
    nota: 7.1,
    nome:'Thor; Ragnarok',
    genero: 'Super Herói'
);

$filmeComoStringJson = json_encode($filme);
file_put_contents(__DIR__.'/filme.json', $filmeComoStringJson);
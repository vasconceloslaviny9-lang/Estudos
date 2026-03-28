<?php

//funções que só realizam ações, mas não geram dados são também chamadas de subRotinas
function exibeMensagemLancamento(int $ano): void{
    if ($ano > 2022) {
        echo "O Filme é lançamento!\n";
        }   
    elseif ($ano > 2022 && $ano <= 2000){
        echo "o Filme ainda é novo\n";
        }
    else {
        echo "O Filme é antigo\n";
    }
}

function incluidoNoPlano(bool $plano, int $ano): bool{ 
    return $plano || $ano <= 2000;
}

function criarFilme(string $nome, int $ano, float $nota, string $genero):array{
    return[
        'nome' => $nome,
        'ano' => $ano,
        'nota' => $nota,
        'genero' => $genero,
    ];
}



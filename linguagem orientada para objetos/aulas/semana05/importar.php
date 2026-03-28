<?php
$caminhoDoArquivo = __DIR__.'/filme.json';
$conteudoArquivoFilme = file_get_contents($caminhoDoArquivo);
$filme = json_decode($conteudoArquivoFilme, true);

var_dump($filme);
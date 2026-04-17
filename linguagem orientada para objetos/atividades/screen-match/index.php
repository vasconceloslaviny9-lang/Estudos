<?php
require __DIR__ ."/src/Modelo/Genero.php";
require __DIR__ . "/src/Modelo/Filme.php";


echo"Bem-vindo ao screen Match\n";

$filme1 = new Filme(
    'Thor Ragnarok',
    2021,
    Genero::SeperHeroi
);

$filme2 = new Filme(
    'Top Gun Maverick',
    2018,
    Genero::Acao
);
$filme1->avalia(10);
$filme2->avalia(6);
$filme1->avalia(8);



var_dump($filme1);
echo $filme1->media();

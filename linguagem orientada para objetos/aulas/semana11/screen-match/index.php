<?php

require __DIR__ . "/src/Model/Genero.php";
require __DIR__ . "/src/Model/Titulo.php";
require __DIR__ . "/src/Model/Serie.php";
require __DIR__ . "/src/Model/Filme.php";


echo "Bem-vindo ao Screen Match\n";

$filme1 = new Filme(
    'Thor Ragnarok',
    2021,
    Genero::SuperHeroi,
    180
);

$serie1 = new Serie(
    'The Boys',
    2017,
    Genero::Acao,
    5,
    11,
    60
);

$serie1->avaliar(10);
$serie1->avaliar(5);

var_dump($serie1);
echo $serie1->media();


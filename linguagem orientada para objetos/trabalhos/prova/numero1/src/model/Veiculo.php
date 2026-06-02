<?php
abstract class Veiculo {
public function __construct(
public readonly string $marca,
public readonly string $modelo,
public readonly int $anoFabricacao,
public readonly TipoCombustivel $combustivel

) {}
abstract public function calcularTaxa(): float;
}
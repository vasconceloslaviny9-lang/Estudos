<?php
abstract class Produto {
public function __construct(
public readonly string $nome,
public readonly int $precoBase,
public readonly CategoriaEletronica $categoria_eletronica

) {}
abstract public function calcularTaxaEnvio(): float;
}
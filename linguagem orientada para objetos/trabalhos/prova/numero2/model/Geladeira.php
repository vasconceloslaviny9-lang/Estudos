<?php
class Geladedira extends Produto {
public function __construct(
int $qntMesesGarantia
TipoCombustivel $combustivel,
public readonly int $qtdPassageiros
) {
parent::__construct($marca, $modelo, $anoFabricacao);
}
public function calcularTaxa(): float {
return $this->qtdPassageiros * 35.00;
}
}
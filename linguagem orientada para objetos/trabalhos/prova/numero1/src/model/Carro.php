<?php
class Carro extends Veiculo {
public function __construct(
string $marca,
string $modelo,
int $anoFabricacao,
TipoCombustivel $combustivel,
public readonly int $qtdPassageiros
) {
parent::__construct($marca, $modelo, $anoFabricacao, $combustivel);
}
public function calcularTaxa(): float {
return $this->qtdPassageiros * 35.00;
}
}
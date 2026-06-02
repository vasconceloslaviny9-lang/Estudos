<?php
class CalculadoraDeIPVA {
private float $totalImpostos = 0;
public function incluirNoCalculo(Veiculo $veiculo): void {
$this->totalImpostos += $veiculo->calcularTaxa();
}
public function getTotal(): float {
return $this->totalImpostos;
}
}
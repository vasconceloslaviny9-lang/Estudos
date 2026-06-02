<?php
class CalculadoraDeFrete {
private float $totalImpostos = 0;
public function incluirNoCalculo(Produto $produto): void {
$this->totalImpostos += $produto->calcularTaxa();
}
public function getTotal(): float {
return $this->totalImpostos;
}
}
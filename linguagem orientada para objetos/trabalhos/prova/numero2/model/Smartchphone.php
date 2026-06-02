<?php
class Smartchphone extends Produto {

public function __construct(
string $nome,
string $precoBase,
CategoriaEletronica $categoria,
public readonly int $qtdAcessorios,
) {
parent::__construct($nome, $precoBase, $categoria);
}
public function calcularTaxa(): float {
return $this->qtdPassageiros * 35.00;
}
}
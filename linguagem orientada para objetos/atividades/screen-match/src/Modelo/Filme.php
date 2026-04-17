<?php
class Filme{
    private array $notas;

    public function __construct(
         public string $nome,
         public int $anoLancamento,
         public Genero $genero,
    )
    {
        $this-> notas = [];
    }
    public function avalia($notas): void
    {
        $this->notas[]= $notas;
    }
    public function media():float{
        $somaNotas = array_sum($this->notas);
        $quantidadeNotas = count($this->notas);

        return $somaNotas / $quantidadeNotas;
    }
}
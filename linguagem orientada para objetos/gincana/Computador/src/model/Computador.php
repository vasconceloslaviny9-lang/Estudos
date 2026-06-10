<?php
class Computador{
    public function __construct(
        public readonly Situacao $Situacao,
        public readonly MARCA $Marca,
        public readonly string $descricao

    )
    {}
}
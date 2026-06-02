<?php

class Serie extends Titulo {

    public function __construct(
        string $nome,
        int $anoLancamento,
        Genero $genero,
        public readonly  int $temporada,
        public readonly int $qtdEpisodioPorTemporada,
        public readonly int $duracaoPorEpisodio
    )
    {
        parent:: __construct ($nome, $anoLancamento, $genero);
    }

     public function duracaoEmMinutos():int{
        return $this->temporada * $this->qtdEpisodioPorTemporada * $this->duracaoPorEpisodio;
}
}
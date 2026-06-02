<?php

class calculadoraDeMaratona{
    private int $duracaoDeMaratona;

    public function incluir (Titulo $titulo):void{
        $this->duracaoDeMaratona += $titulo->duracaoEmMinutos();
    }

    public function getDuracao(){
        return $this->duracaoDeMaratona;
    }

}
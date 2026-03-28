<?php
$saldo = 1000;
echo "Bem-Vindo ao se banco!\n";
echo "Titular da Conta: Laviny Vasconcelos\n";
echo "Saldo inicial = R$ 1000\n";

do {
    echo "******************************\n";
echo "Escolha opção no menu abaixo:\n";
echo "1 - Consultar Saldo\n";
echo "2 - Saque\n";
echo "3 - Depósito\n";
echo "4 - Sair\n";
echo "******************************\n";

$opcao = (float)fgets(STDIN);

switch ($opcao) {
    case 1:
        echo $titular = "Laviny Vasconcelos\n";
        echo "Seu saldo é de r$ $saldo\n";
        break;
    case 2:
        echo "Qual valor deseja sacar?\n";
        $saque = (float)fgets(STDIN);
        if($saque > $saldo){
            echo "Saldo insuficiente \n";
        }
        else{ 
            $saldo = $saldo - $saque;
            echo $saldo;
        }
        
        break;
    case 3:
        echo "Qual o valor depositado?\n";
        $deposito = (float)fgets(STDIN);
        $saldo = $saldo + $deposito;
        echo "Seu saldo é: $saldo \n";
        break;
    case 4:
        echo "Adeus\n";
        break;
    default:
        echo "Opção inválida\n";
}
    
} while ($opcao !=4);


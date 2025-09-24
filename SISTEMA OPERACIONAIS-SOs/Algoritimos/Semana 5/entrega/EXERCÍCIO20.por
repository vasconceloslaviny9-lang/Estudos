programa
{
  
    const cadeia NOME_MONSTRO_PADRAO = "Cyclops"
    const inteiro XP_POR_MONSTRO_X = 150
    const real GP_MEDIO_POR_MONSTRO_X = 25.50
    const real PESO_LOOT_MEDIO_POR_MONSTRO_X = 3.2

  
    cadeia nome_personagem
    inteiro quantidade_monstros_derrotados
    real tempo_gasto_horas
    real custo_suprimentos

    
    inteiro xp_total_ganha
    real gp_total_coletado
    real peso_total_loot
    real lucro_prejuizo_cacada
    real xp_por_hora
    real gp_por_hora

    funcao inicio()
    {
       
        escreva("--- Relatório Detalhado de Caçada no Tibia ---\n")
        escreva("Monstro Caçado: ", NOME_MONSTRO_PADRAO, "\n\n")

        escreva("Nome do seu Personagem: ")
        leia(nome_personagem)

        escreva("Quantos ", NOME_MONSTRO_PADRAO, "(s) você derrotou? ")
        leia(quantidade_monstros_derrotados)

        escreva("Tempo total gasto na caçada (em horas, ex: 1.5 para 1h30min): ")
        leia(tempo_gasto_horas)

        escreva("Custo total dos suprimentos (poções, etc.) em GPs: ")
        leia(custo_suprimentos)

        
        xp_total_ganha = quantidade_monstros_derrotados * XP_POR_MONSTRO_X

        
        gp_total_coletado = quantidade_monstros_derrotados * GP_MEDIO_POR_MONSTRO_X

     
        peso_total_loot = quantidade_monstros_derrotados * PESO_LOOT_MEDIO_POR_MONSTRO_X

       
        lucro_prejuizo_cacada = gp_total_coletado - custo_suprimentos

      
        xp_por_hora = xp_total_ganha / tempo_gasto_horas
        gp_por_hora = gp_total_coletado / tempo_gasto_horas
        
      
        escreva("\n\n--- Relatório da Caçada de ", nome_personagem, " ---\n")
        escreva("Monstro Focado: ", NOME_MONSTRO_PADRAO, "\n")
        escreva("Quantidade Derrotada: ", quantidade_monstros_derrotados, "\n")
        escreva("Tempo da Caçada: ", tempo_gasto_horas, " horas\n")
        escreva("--------------------------------------------------\n")
        escreva("XP Total Ganhada: ", xp_total_ganha, " pontos de experiência\n")
        escreva("GP Total Estimado Coletado: ", gp_total_coletado, " GPs\n")
        escreva("Peso Estimado do Loot: ", peso_total_loot, " Oz\n")
        escreva("--------------------------------------------------\n")
        escreva("Custo dos Suprimentos: ", custo_suprimentos, " GPs\n")
        escreva("Lucro/Prejuízo Estimado: ", lucro_prejuizo_cacada, " GPs\n")
        escreva("--------------------------------------------------\n")
        escreva("Média de XP por Hora: ", xp_por_hora, " XP/h\n")
        escreva("Média de GP por Hora: ", gp_por_hora, " GP/h\n")
        escreva("--------------------------------------------------\n")
        escreva("Bom jogo, ", nome_personagem, "!\n")
    }
}

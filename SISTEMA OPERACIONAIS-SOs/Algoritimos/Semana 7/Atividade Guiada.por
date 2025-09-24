programa
{
    real nota_prova
    real nota_trabalho
    real media_semestral
    const real media_aprovacao= 7.0
    logico atingiu_media_minima

    funcao inicio()
    {
        escreva("--- Calculadora de Média Semestral ---\n")
        escreva("Digite a nota da Prova: ")
        leia(nota_prova)
        escreva("Digite a nota do Trabalho: ")
        leia(nota_trabalho)

        // Cálculo aritmético da média
        media_semestral = (nota_prova + nota_trabalho) / 2.0

        // Verificação relacional para o status
        atingiu_media_minima = (media_semestral >= media_aprovacao)

        escreva("\n--- Boletim do Aluno ---\n")
        escreva("Nota da Prova: ", nota_prova, "\n")
        escreva("Nota do Trabalho: ", nota_trabalho, "\n")
        escreva("Média Semestral Calculada: ", media_semestral, "\n")
        escreva("Atingiu a média de aprovação (", media_aprovacao, ")? ", atingiu_media_minima, "\n")
    }
}
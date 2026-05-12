programa
{
    funcao inicio()
    {
        // Declaração de variáveis (No Portugol, definimos os tipos no início)
        real num1, num2, resultado
        caracter operador

        escreva("Calculadora Simples\n")

        escreva("Digite o primeiro número: ")
        leia(num1)

        escreva("Digite o operador (+, -, *, /): ")
        leia(operador)

        escreva("Digite o segundo número: ")
        leia(num2)

        // Estrutura de decisão (Equivalente ao if/elif/else)
        se (operador == "+") 
        {
            resultado = num1 + num2
            escreva("O resultado é: ", resultado)
        }
        senao se (operador == "-")
        {
            resultado = num1 - num2
            escreva("O resultado é: ", resultado)
        }
        senao se (operador == "*")
        {
            resultado = num1 * num2
            escreva("O resultado é: ", resultado)
        }
        senao se (operador == "/")
        {
            // Uma pequena melhoria: evitar divisão por zero
            se (num2 != 0) {
                resultado = num1 / num2
                escreva("O resultado é: ", resultado)
            } senao {
                escreva("Erro: Divisão por zero!")
            }
        }
        senao
        {
            escreva("Operador inválido!")
        }
    }
}
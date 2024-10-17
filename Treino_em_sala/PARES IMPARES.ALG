Algoritmo "Pares Impares"
// 
//  
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 8/8/2024
Var
// Seção de Declarações das variáveis 
num1, num2, num3: inteiro
pares, impares: inteiro

Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 
pares <- 0
impares <- 0

escreva("Digite o primeiro numero: ")
leia(num1)
escreva("Digite o segundo numero: ")
leia(num2)
escreva("Digite o terceiro numero: ")
leia(num3)

se num1 % 2 = 0 entao
   pares <- pares + 1
senao
   impares <- impares + 1
fimse

se num2 % 2 = 0 entao
   pares <- pares + 1
senao
   impares <- impares + 1
fimse

se num3 % 2 = 0 entao
   pares <- pares + 1
senao
   impares <- impares + 1
fimse

escreval("pares:" , pares)

escreva("impares:" , impares)

Fimalgoritmo
Algoritmo "TipoTriangulo"
// 
//  
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 8/8/2024
Var
// Seção de Declarações das variáveis 
ladoA, ladoB, ladoC: real


Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 
escreva("Digite o valor do lado A: ")
leia(ladoA)
escreva("Digite o valor do lado B: ")
leia(ladoB)
escreva("Digite o valor do lado C: ")
leia(ladoC)

se (ladoA < (ladoB + ladoC)) e (ladoB < (ladoA + ladoC)) e (ladoC < (ladoA + ladoB)) entao
   se(ladoA = ladoB) e (ladoB = ladoC) entao
     escreva("Equiltero")
   senao
     se(ladoA = ladoB) ou (ladoB = ladoC) ou (ladoA = ladoC) entao
     escreva("Isosceles")
     senao
     escreva("escaleno")
     fimse
   fimse



senao
     escreva("Nao triangulo")
fimse



Fimalgoritmo
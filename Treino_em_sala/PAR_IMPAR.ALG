Algoritmo "Par_Impar"
// 
//  
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 13/8/2024
Var
numero: real

Inicio
escreval("Digite um numero: ")
leia(numero)

se (numero % 2 = 0) entao
   se (numero < 100)entao
      escreval("E par e menor que 100.")
   senao
        escreval("E par e maior ou igual a 100.")
   fimse
fimse

se (numero % 2 = 1) entao
   se (numero < 100)entao
      escreval("E impar e menor que 100.")
   senao
        escreval("E impar e maior ou igual a 100.")
   fimse
fimse

Fimalgoritmo
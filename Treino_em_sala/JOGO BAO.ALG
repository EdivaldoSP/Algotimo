Algoritmo "Jogo bao"
// 
//  
// Descrição   : Jogo de adivinhaçao
// Autor(a)    : Gian
// Data atual  : 15/3/2024
Var
// Seção de Declarações das variáveis 

X,R, P : real
N : inteiro

Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 

X <- randi(100)
N <- 0

Escreval("Escolha um numero de 0 a 100")

Repita

N <- N + 1

Leia (R)

Se X = R entao
   escreval ("Parabens, voce venceu!!!")
   
Senao
   Se R > X entao
   escreval ("Muito Alto")
   fimse
   
   Se R < X entao
   escreval ("Muito Baixo")
   fimse
fimse
ate X = R

P <- (1000/N)

escreval ("Sua pontuaçao foi",P)

Fimalgoritmo
Algoritmo "Calcular_Idade"

Var
Mercedes, filho1, filho2, calculo1, filho3: inteiro

Inicio
escreval("Digite a idade de Mercedes: ")
leia(mercedes)
escreval("Digite a idade do primeiro filho: ")
leia(filho1)
escreval("Digite a idade do segundo filho: ")
leia(filho2)


calculo1 <- (filho1 + filho2)

filho3 <- (mercedes - calculo1)


se (filho1 >  filho2) e (filho1 > filho3) entao
   escreval("A idade do filho mais velho e: ", filho1)
fimse

se (filho2 >  filho1) e (filho2 > filho3) entao
   escreval("A idade do filho mais velho e: ", filho2)
fimse

se (filho3 >  filho1) e (filho3 > filho2) entao
   escreval("A idade do filho mais velho e: ", filho3)
fimse


   


Fimalgoritmo
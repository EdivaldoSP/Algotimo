Algoritmo "valor_a_ser_pago"
// 
//  
// Descri��o   : Aqui voc� descreve o que o programa faz! (fun��o)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 8/8/2024
Var
// Se��o de Declara��es das vari�veis 
produto: caracter
preco: real
preco_pago: real
forma_de_pagamento: inteiro


Inicio
// Se��o de Comandos, procedimento, fun��es, operadores, etc..

escreva("Nome do produto: ")
leia(produto)
escreva("Pre�o do produto: ")
leia(preco)

escreval("Formas de Pagamento")
escreval("1:A vista em dinheiro, pix, ou debito: 15% de desconto")
escreval("2:Uma parcela no cartao de credito: 10% de desconto")
escreval("3:Duas parcela, pre�o normal da etqueta sem juros")
escreval("4:Tres parcelas: pre�o normal da etiqueta mais juros de 5%")

escreva("Escolha a forma de pagamento do produto: ")
leia(forma_de_pagamento)

se forma_de_pagamento = 1 entao
   preco_pago <- preco - (preco * (15/100))
   escreva("Deve pagar", preco_pago)
fimse

se forma_de_pagamento = 2 entao
   preco_pago <- preco - (preco * (10/100))
   escreva("O valor a ser pago e :", preco_pago)
fimse

se forma_de_pagamento = 3 entao
   preco_pago <- preco / 2
   escreva("O valor a ser pago sera duas parcelas de :", preco_pago)
fimse

se forma_de_pagamento = 4 entao
   preco_pago <- preco + (preco * (5/100))
   escreva("O valor a ser pago sera :", preco_pago)
fimse



Fimalgoritmo
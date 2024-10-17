Algoritmo "valor_a_ser_pago"
// 
//  
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 8/8/2024
Var
// Seção de Declarações das variáveis 
produto: caracter
preco: real
preco_pago: real
forma_de_pagamento: inteiro


Inicio
// Seção de Comandos, procedimento, funções, operadores, etc..

escreva("Nome do produto: ")
leia(produto)
escreva("Preço do produto: ")
leia(preco)

escreval("Formas de Pagamento")
escreval("1:A vista em dinheiro, pix, ou debito: 15% de desconto")
escreval("2:Uma parcela no cartao de credito: 10% de desconto")
escreval("3:Duas parcela, preço normal da etqueta sem juros")
escreval("4:Tres parcelas: preço normal da etiqueta mais juros de 5%")

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
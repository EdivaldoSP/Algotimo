import time
import os
opcao = 0
series_add = { # VARIAVEL TEMPORARIA PARA ARMAZENAR SERIES ADICIONADAS

}

series = [{                 # LISTA DE DICIONARIOS (SERIES CADASTRADAS)
    'nome': 'Friends',
    'ano': 1994,
    'genero': 'comedia',
    'descricao': 'Um grupo de amigos com a visão de ser um líder de comunidade',
}, {
    'nome': 'Game of Thrones',
    'ano': 2011,
    'genero': 'drama',
    'descricao': 'Um jogo de guerra e romance sobre o reinado de um reino',
}, {
    'nome': 'The Big Bang Theory',
    'ano': 2007,
    'genero': 'comedia',
    'descricao': 'Um drama sobre a história do universo',
}, {
    'nome': 'The Office',
    'ano': 2005,
    'genero': 'comedia',
    'descricao': 'Um trabalho de escritório voltado para a supervisão de uma empresa',
}, {
    'nome': 'The Walking Dead',
    'ano': 2005,
    'genero': 'drama',
    'descricao': 'Um grupo de sobreviventes que vive na periferia de uma cidade',
}]

while opcao != 7: # ENQUANTO MINHA VARIAVEL OPCAO FOR DIFERENTE DE 7, PRINTAR O MENU 
    print('{:=^30}'.format('| SEJA BEM VINDO (A) |'))
    print()
    print('{:-^31}'.format('> SISTEMA DE CADASTRO SÉRIE <'))

    print('''
[1] imprimir a lista de séries cadastradas
[2] imprimir trecho específico da lista de séries
[3] inserir uma nova série
[4] deletar série na lista
[5] buscar uma série (utilizando a chave)
[6] editar série (utilizando a chave)
[7] sair do programa
''')
    opcao = input("Escolha uma opção do menu: ")
    os.system("clear") # LIMPANDO O TERMINAL

    # menu de opções
    try: # O CÓDIGO IRÁ RODAR E QUALQUER TIPO DE ERRO IRÁ CAIR NO EXCEPT
        
        opcao_int = int(opcao)

        # opção para  imprimir todas as séries
        if int(opcao_int) == 1:
            try: # O CÓDIGO IRÁ RODAR E QUALQUER TIPO DE ERRO IRÁ CAIR NO EXCEPT

                for i in range(0, len(series)): # PERCORRER A LISTA DE SÉRIES E PRINTA CADA DICIONÁRIO.
                    print("-----" * 30)
                    print(f"{i+1}ª SÉRIE:\nNome: {series[i]['nome']} \nAno: {series[i]['ano']} \nGênero: {series[i]['genero']} \nDescrição: {series[i]['descricao']}\n")
                print("-----" * 30)

                # OPÇÃO DE VOLTAR AO MENU OU FINALIZAR O PROGRAMA
                menu = input("Deseja voltar para o menu? y= sim, n= finaliza programa [y | n]: ")
                if menu.lower() == 'y':
                    os.system("clear")
                    continue
                            
                elif menu.lower() == 'n':
                    break
                else:
                    os.system("clear") # LIMPANDO O TERMINAL
                    print('{:-^100}'.format("\n| ERRO. VOLTANDO PARA O MENU... |\n"))
                    time.sleep(1)
                       
            except:
                print('{:-^70}'.format("\n| ERRO AO IMPRIMIR A LISTA DE SÉRIES. |\n"))

        # opção para imprimir um intervalo da das séries listadas
        elif int(opcao_int) == 2:
            try: # O CÓDIGO IRÁ RODAR E QUALQUER TIPO DE ERRO IRÁ CAIR NO EXCEPT

                inicio = int(input("Início do trecho a ser impresso: "))
                fim = int(input("Fim do trecho a ser impresso: "))
                if inicio >= 0  and fim <= len(series): # VERIFICA SE O INTERVALO É VÁLIDO
                    for i in range(inicio - 1, fim): # PERCORRE A LISTA DE SÉRIES COM OS ÍNDICES DE ENTRADA
                        print("-----" * 30)
                        print(f"{i+1}ª SÉRIE:\nNome: {series[i]['nome']} \nAno: {series[i]['ano']} \nGênero: {series[i]['genero']} \nDescrição: {series[i]['descricao']}")
                        print("-----" * 30)

                    # OPÇÃO DE VOLTAR AO MENU OU FINALIZAR O PROGRAMA
                    menu = input("Deseja voltar para o menu? y= sim, n= finaliza programa [y | n]: ")
                    if menu.lower() == 'y':
                        os.system("clear")
                        continue
                    elif menu.lower() == 'n':
                        break   
                    else:
                        os.system("clear")
                        print('{:-^70}'.format("\n| ERRO. VOLTANDO PARA O MENU... |\n"))
                        time.sleep(1)
                   
                else:
                    print('{:-^120}'.format("\n| INTERVALO INVÁLIDO. TENTE NOVAMENTE |\n"))
                    
            except:
                print('{:-^190}'.format("\n| ERRO AO IMPRIMIR O TRECHO ESPECÍFICO DA LISTA DE SÉRIES. |\n"))

        # opção para cadastrar uma nova série
        elif int(opcao_int) == 3:
            try: # O CÓDIGO IRÁ RODAR E QUALQUER TIPO DE ERRO IRÁ CAIR NO EXCEPT

                if len(series) <=50: # VERIFICA SE O LIMITE DE SÉRIES CADASTRADAS ULTRAPASSOU

                    # ADICIONA UMA NOVA SÉRIE NA VARIÁVEL TEMPORARIA (series_add)
                    for i in range(1): 
                        series_add['nome'] = str(input("Digite o nome da série: "))
                        series_add['ano'] = int(input("Digite o ano de lançamento: "))
                        series_add['genero'] = str(input("Digite o gênero: "))
                        series_add['descricao'] = str(input("Digite a descrição: "))
                        series.append(series_add.copy()) # ADICIONA AS SÉRIES A LISTA 
                    time.sleep(1)
                    print('{:-^98}'.format("\n| SÉRIE ADICIONADA COM SUCESSO |\n"))
                    
                    # OPÇÃO DE VOLTAR AO MENU OU FINALIZAR O PROGRAMA
                    menu = input("Deseja voltar para o menu? y= sim, n= finaliza programa [y | n]: ")
                    if menu.lower() == 'y':
                        os.system("clear")
                        continue
                            
                    elif menu.lower() == 'n':
                        break
                    else:
                        os.system("clear")
                        print('{:-^80}'.format("\n| ERRO. VOLTANDO PARA O MENU... |\n"))
                        time.sleep(1)
                        
                else:
                    os.system("clear")
                    print("LIMITE DE SÉRIES ATINGIDO. IMPOSSÍVEL ADICIONAR MAIS SÉRIES.")
 
            except:
                print('{:-^102}'.format("\n| ERRO AO INSERIR A NOVA SÉRIE. |\n"))

        # opção para deletar uma série cadastrada sem usar break
        elif int(opcao_int) == 4:
            try: # O CÓDIGO IRÁ RODAR E QUALQUER TIPO DE ERRO IRÁ CAIR NO EXCEPT

                encontrar_series_1 = False # VARIVAEL FLAG COMO FALSE
                print("SÉRIES A SEREM DELETADAS:") 
                for i in range(0, len(series)): # PRINT AS SÉRIES DENTRO DA LISTA
                    print(f"{i+1}ª SÉRIE:\nNome: {series[i]['nome']} \nAno: {series[i]['ano']} \nGênero: {series[i]['genero']} \nDescrição: {series[i]['descricao']}\n")

                deletar = input("DIGITE O NOME (CHAVE) DA SÉRIE PARA DELETAR: ")
                i = 0
                while i < len(series) and not encontrar_series_1: # VERIFICA CADA INDICE (SERIE) NA LISTA  
                    if (series[i]['nome']).lower() == deletar.lower(): # SE ENCONTRAR, ELE DELETA
                        encontrar_series_1 = True
                        del series[i]
                        print("APAGANDO...")
                        time.sleep(1) # DELAY DE 1 SEC.
                        print('{:-^98}'.format("\n| SÉRIE DELETADA COM SUCESSO! |\n"))
        
                    else: # SENAO, ELE VAI ADICIONANDO + 1 A VARIAVEL "i" ATE PERCORRER TODOS OS ITENS NA LISTA
                        i += 1
                if not encontrar_series_1:
                        print('{:-^136}'.format("\n| SÉRIE NÃO ENCONTRADA. TENTE NOVAMENTE... |\n"))

                # OPÇÃO DE VOLTAR AO MENU OU FINALIZAR O PROGRAMA     
                menu = input("Deseja voltar para o menu? y= sim, n= finaliza programa [y | n]: ")
                if menu.lower() == 'y':
                    os.system("clear")
                    continue
                elif menu.lower() == 'n':
                    break
                else:
                    os.system("clear")
                    print('{:-^98}'.format("\n| ERRO. VOLTANDO PARA O MENU... |\n"))
                    time.sleep(1)
                
            except:
                print('{:-^98}'.format("\n| ERRO AO DELETAR A SÉRIE. |\n"))


        # opção para buscar uma série cadastrada sem usar o break
        elif int(opcao_int) == 5:
            try: # O CÓDIGO IRÁ RODAR E QUALQUER TIPO DE ERRO IRÁ CAIR NO EXCEPT

                encontrar_series_2 = False # MESMA LÓGICA DA OPÇÃO ANTERIOR
                buscar = str(input("DIGITE O NOME (CHAVE) PARA REALIZAR A BUSCA: "))
                for i in range(0, len(series)):
                    if (series[i]['nome']).lower() == buscar.lower():
                        encontrar_series_2 = True
                        print("Buscando...")
                        time.sleep(1)
                        print('{:-^70}'.format("\n| SÉRIE ENCONTRADA! |\n"))                    
                        print("-----" * 30)
                        print(f"\nNome: {series[i]['nome']} \nAno: {series[i]['ano']} \nGênero: {series[i]['genero']} \nDescrição: {series[i]['descricao']}\n")
                        print("-----" * 30)
        
                if not encontrar_series_2:
                    os.system("clear")
                    print('{:-^136}'.format("\n| SÉRIE NÃO ENCONTRADA. TENTE NOVAMENTE... |\n")) 

                # OPÇÃO DE VOLTAR AO MENU OU FINALIZAR O PROGRAMA
                menu = input("Deseja voltar para o menu? y= sim, n= finaliza programa [y | n]: ")
                if menu.lower() == 'y':
                    os.system("clear")
                    continue
                elif menu.lower() == 'n':
                    break
                else:
                    os.system("clear")
                    print('{:-^98}'.format("\n| ERRO. VOLTANDO PARA O MENU... |\n"))
                    time.sleep(1)
                
            except:
                print('{:-^70}'.format("\n| ERRO AO BUSCAR A SÉRIE. |\n")) 

        # opção para editar uma série sem usar break
        elif int(opcao_int) == 6:
            try: # O CÓDIGO IRÁ RODAR E QUALQUER TIPO DE ERRO IRÁ CAIR NO EXCEPT

                encontrar_series_3 = False
                mudar = str(input("DIGITE O NOME (CHAVE) PARA EDITAR A SÉRIE: "))
                for i in range(0, len(series)): # VAI PROCURAR A SÉRIE NA LISTA
                    if (series[i]['nome']).lower() == mudar.lower(): # SE ENCONTRAR, ENTÃO VAI CONTINUAR O CÓD.
                        encontrar_series_3 = True
                        print("Buscando...")
                        time.sleep(1)
                        print('{:-^70}'.format("\n| SÉRIE ENCONTRADA! |\n")) 
                        print('''
Opções:
    [1] Mudar nome
    [2] Mudar data de lançamento
    [3] Mudar gênero
    [4] Mudar descrição
''')
                        # MENU DE EDIÇÃO DA SÉRIE
                        alterar = input("O que deseja alterar? ")
                        if alterar == '1':
                            series[i]['nome'] = str(input("Digite o novo nome: "))
                            print('{:-^98}'.format("\n| SÉRIE ATUALIZADA COM SUCESSO! |\n")) 
                        elif alterar == '2':
                            series[i]['ano'] = int(input("Digite a nova data de lançamento: "))
                            print('{:-^98}'.format("\n| SÉRIE ATUALIZADA COM SUCESSO! |\n")) 
                        elif alterar == '3':
                            series[i]['genero'] = str(input("Digite o novo genero: "))
                            print('{:-^98}'.format("\n| SÉRIE ATUALIZADA COM SUCESSO! |\n")) 
                        elif alterar == '4':
                            series[i]['descricao'] = str(input("Digite a nova descrição: "))
                            print('{:-^98}'.format("\n| SÉRIE ATUALIZADA COM SUCESSO! |\n")) 
                        else:
                            print('{:-^110}'.format("\n| OPÇÃO INVÁLIDA. TENTE NOVAMENTE! |\n"))
                        time.sleep(1)
                        
                
                if not encontrar_series_3:
                    os.system("clear")
                    print('{:-^136}'.format("\n| SÉRIE NÃO ENCONTRADA. TENTE NOVAMENTE... |\n"))

                # OPÇÃO DE VOLTAR AO MENU OU FINALIZAR O PROGRAMA       
                menu = input("Deseja voltar para o menu? y= sim, n= finaliza programa [y | n]: ")
                if menu.lower() == 'y':
                    os.system("clear")
                    continue
                elif menu.lower() == 'n':
                    break
                else:
                    os.system("clear")
                    print('{:-^70}'.format("\n| ERRO. VOLTANDO PARA O MENU... |\n"))
                    time.sleep(1)

            except:
                print('{:-^70}'.format("\n| ERRO AO BUSCAR A SÉRIE. |\n"))
        
        # opção para sair do programa
        elif int(opcao_int) == 7:
            opcao = 7

    except:
        print('{:-^114}'.format("\n| OPÇÃO INVÁLIDA. TENTE NOVAMENTE! |\n"))
print('{:-^70}'.format("\n| FINALIZANDO... |\n"))
time.sleep(1)
print('{:-^70}'.format("\n| FIM DO PROGRAMA. |\n"))
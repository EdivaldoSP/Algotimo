import time
import os
opcao = 0
series_add = {

}

series = [{
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

while opcao != 7:
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
    os.system("clear")

    # menu de opções
    try:
        opcao_int = int(opcao)

        # opção para  imprimir todas as séries
        if int(opcao_int) == 1:
            try:
                for i in range(0, len(series)):
                    print("-----" * 30)
                    print(f"{i+1}ª SÉRIE:\nNome: {series[i]['nome']} \nAno: {series[i]['ano']} \nGênero: {series[i]['genero']} \nDescrição: {series[i]['descricao']}\n")
                print("-----" * 30)

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
                print('{:-^70}'.format("\n| ERRO AO IMPRIMIR A LISTA DE SÉRIES. |\n"))

        # opção para imprimie um intervalo da das séries listadas
        elif int(opcao_int) == 2:
            try:
                inicio = int(input("Início do trecho a ser impresso: "))
                fim = int(input("Fim do trecho a ser impresso: "))
                if inicio >= 0  and fim <= len(series):
                    for i in range(inicio-1, fim):
                        print("-----" * 30)
                        print(f"{i+1}ª SÉRIE:\nNome: {series[i]['nome']} \nAno: {series[i]['ano']} \nGênero: {series[i]['genero']} \nDescrição: {series[i]['descricao']}")
                        print("-----" * 30)
        
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
            try:
                if len(series) <=50:
                    for i in range(1):
                        series_add['nome'] = str(input("Digite o nome da série: "))
                        series_add['ano'] = int(input("Digite o ano de lançamento: "))
                        series_add['genero'] = str(input("Digite o gênero: "))
                        series_add['descricao'] = str(input("Digite a descrição: "))
                        series.append(series_add.copy())
                    time.sleep(1)
                    print('{:-^98}'.format("\n| SÉRIE ADICIONADA COM SUCESSO |\n"))
                    
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

        # opção para deletar uma série cadastrada 
        elif int(opcao_int) == 4:
            try:
                encontrar_series_1 = False
                print("SÉRIES A SEREM DELETADAS:") 
                for i in range(0, len(series)):
                    print(f"{i+1}ª SÉRIE:\nNome: {series[i]['nome']} \nAno: {series[i]['ano']} \nGênero: {series[i]['genero']} \nDescrição: {series[i]['descricao']}\n")

                deletar = input("DIGITE O NOME (CHAVE) DA SÉRIE PARA DELETAR: ")
                i = 0
                while i < len(series) and not encontrar_series_1:
                    if (series[i]['nome']).lower() == deletar.lower():
                        encontrar_series_1 = True
                        del series[i]
                        print("APAGANDO...")
                        time.sleep(1)
                        print('{:-^98}'.format("\n| SÉRIE DELETADA COM SUCESSO! |\n"))
        
                    else:
                        i += 1
                if not encontrar_series_1:
                        print('{:-^136}'.format("\n| SÉRIE NÃO ENCONTRADA. TENTE NOVAMENTE... |\n"))
                        
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


        # opção para buscar uma série cadastrada
        elif int(opcao_int) == 5:
            try:
                encontrar_series_2 = False
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

        # opção para editar uma série
        elif int(opcao_int) == 6:
            try:
                encontrar_series_3 = False
                mudar = str(input("DIGITE O NOME (CHAVE) PARA EDITAR A SÉRIE: "))
                for i in range(0, len(series)):
                    if (series[i]['nome']).lower() == mudar.lower():
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
                        alterar = input("O que deseja alterar? ")
                        if alterar == '1':
                            series[i]['nome'] = str(input("Digite o novo nome: "))
                        elif alterar == '2':
                            series[i]['ano'] = int(input("Digite a nova data de lançamento: "))
                        elif alterar == '3':
                            series[i]['genero'] = str(input("Digite o novo genero: "))
                        elif alterar == '4':
                            series[i]['descricao'] = str(input("Digite a nova descrição: "))
                        time.sleep(1)
                        print('{:-^98}'.format("\n| SÉRIE ATUALIZADA COM SUCESSO! |\n")) 
                
                if not encontrar_series_3:
                    os.system("clear")
                    print('{:-^136}'.format("\n| SÉRIE NÃO ENCONTRADA. TENTE NOVAMENTE... |\n"))
                        
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

    except ValueError:
        print('{:-^114}'.format("\n| OPÇÃO INVÁLIDA. TENTE NOVAMENTE! |\n"))
print('{:-^70}'.format("\n| FINALIZANDO... |\n"))
time.sleep(1)
print('{:-^70}'.format("\n| FIM DO PROGRAMA. |\n"))
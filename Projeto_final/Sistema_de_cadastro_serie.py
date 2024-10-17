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
            except:
                print("Erro ao imprimir a lista de séries.")

        # opção para imprimie um intervalo da das séries listadas
        elif int(opcao_int) == 2:
            try:
                inicio = int(input("Início do trecho a ser impresso: "))
                fim = int(input("Fim do trecho a ser impresso: "))
                if inicio >= 0  and fim <= len(series):
                    for i in range(inicio-1, fim):
                        print(f"{i+1}ª SÉRIE:\nNome: {series[i]['nome']} \nAno: {series[i]['ano']} \nGênero: {series[i]['genero']} \nDescrição: {series[i]['descricao']}\n")
                else:
                    print("INTERVALO INVÁLIDO. TENTE NOVAMENTE")
                    
            except:
                print("Erro ao imprimir o trecho específico da lista de séries.")

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
                else:
                    Limite = "LIMITE DE SÉRIES ATINGIDO. IMPOSSÍVEL ADICIONAR MAIS SÉRIES."
                    limite_maior = Limite.upper()
                    print(limite_maior)
            except:
                print("Erro ao inserir a nova série.")

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
                        print(f"SÉRIE {deletar} DELETADA COM SUCESSO!")
                    else:
                        i += 1
                if not encontrar_series_1:
                        tente = "SÉRIE NÃO ENCONTRADA. TENTE NOVAMENTE..."
            except:
                print("Erro ao deletar a série.")

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
                        print(f"Nome: {series[i]['nome']} \nAno: {series[i]['ano']} \nGênero: {series[i]['genero']} \nDescrição: {series[i]['descricao']}\n")
                        print()
                if not encontrar_series_2:
                    print("SÉRIE NÃO ENCONTRADA. TENTE NOVAMENTE...")
            except:
                print("Erro ao buscar a série.")

        # opção para editar uma série
        elif int(opcao_int) == 6:
            try:
                encontrar_series_3 = False
                mudar = str(input("DIGITE O NOME (CHAVE) PARA EDITAR A SÉRIE: "))
                for i in range(0, len(series)):
                    if (series[i]['nome']).lower() == mudar.lower():
                        encontrar_series_3 = True
                        print("Buscando...")
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
                        
                        print()
                if not encontrar_series_3:
                    print("SÉRIE NÃO ENCONTRADA. TENTE NOVAMENTE...")
            except:
                print("Erro ao buscar a série.")
        
        # opção para sair do programa
        elif int(opcao_int) == 7:
            print("Finalizando")
            opcao = 7

    except ValueError:
        print("OPÇÃO INVÁLIDA. TENTE NOVAMENTE")    
print('FIM DO PROGRAMA.')
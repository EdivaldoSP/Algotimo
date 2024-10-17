import time
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

while opcao != 6:
    print('{:=^30}'.format('| SEJA BEM VINDO (A) |'))
    print()
    print('{:-^31}'.format('> SISTEMA DE CADASTRO SÉRIE <'))

    print('''
[1] imprimir a lista de séries cadastradas
[2] imprimir trecho específico da lista de séries
[3] inserir uma nova série
[4] deletar série na lista
[5] buscar uma série (utilizando a chave)
[6] sair do programa
''')
    opcao = input("Escolha uma opção do menu: ")

    if opcao.isalpha() == False:
        opcao_int = int(opcao)
        if int(opcao_int) == 1:
            for i in range(0, len(series)):
                print(f"{i+1}ª SÉRIE:\nNome: {series[i]['nome']} \nAno: {series[i]['ano']} \nGênero: {series[i]['genero']} \nDescrição: {series[i]['descricao']}\n")
            
        elif int(opcao_int) == 2:
            inicio = int(input("Início do trecho a ser impresso: "))
            fim = int(input("Fim do trecho a ser impresso: "))
            if inicio >= 0  and fim <= len(series):
                for i in range(inicio-1, fim):
                    print(f"{i+1}ª SÉRIE:\nNome: {series[i]['nome']} \nAno: {series[i]['ano']} \nGênero: {series[i]['genero']} \nDescrição: {series[i]['descricao']}\n")
            else:
                    print("Intervalo inválido. Tente novamente")

        elif int(opcao_int) == 3:
            if len(series) <=50:
                for i in range(1):
                    series_add['nome'] = str(input("Digite o nome da série: "))
                    series_add['ano'] = int(input("Digite o ano de lançamento: "))
                    series_add['genero'] = str(input("Digite o gênero: "))
                    series_add['descricao'] = str(input("Digite a descrição: "))
                    series.append(series_add.copy())
            else:
                print("Limite de séries atingido. Impossível adicionar mais séries.")

        elif int(opcao_int) == 4:
            encontrar_series_1 = False
            print("SÉRIES A SEREM DELETADAS:") 
            for i in range(0, len(series)):
                print(f"{i+1}ª SÉRIE:\nNome: {series[i]['nome']} \nAno: {series[i]['ano']} \nGênero: {series[i]['genero']} \nDescrição: {series[i]['descricao']}\n")

            deletar = input("Digite o nome (chave) da série para deletar: ")
            i = 0
            while i < len(series) and not encontrar_series_1:
                if (series[i]['nome']) == deletar:
                    encontrar_series_1 = True
                    del series[i]
                    print("Apagando...")
                    time.sleep(1)
                    print(f"Série {deletar} deletada com sucesso!")
                else:
                    i += 1
            if not encontrar_series_1:
                print("Série não encontrada. Tente novamente...")

        elif int(opcao_int) == 5:
            encontrar_series_2 = False
            buscar = str(input("Digite o nome (chave) para realizar a busca: "))
            for i in range(0, len(series)):
                if (series[i]['nome']) == buscar:
                    encontrar_series_2 = True
                    print("Buscando...")
                    time.sleep(1)
                    print(f"Nome: {series[i]['nome']} \nAno: {series[i]['ano']} \nGênero: {series[i]['genero']} \nDescrição: {series[i]['descricao']}\n")
            if not encontrar_series_2:
                print("Série não encontrada. Tente novamente...")

        elif int(opcao_int) == 6:
            print("Finalizando")
 
    else:
        print("Opção inválida. Tente novamente")       
print('Fim do programa.')
from aula1 import (
    #menu,
    cadastrar_caminhao, 
    listar_caminhoes,
    procurar_placa,
    procurar_motorista,
    procurar_cidade,
    procurar_estado,
    procurar_carga,
    alterar_caminhao,
    remover_caminhao,
    estatisticas

)


while True:
    print()
    print("================================")
    print("       SISTEMA DE FROTA")
    print("================================")
    print("1 - Cadastrar caminhão")
    print("2 - Listar caminhões")
    print("3 - Pesquisar por placa")
    print("4 - Pesquisar por motorista")
    print("5 - Pesquisar por cidade")
    print("6 - Pesquisar por estado")
    print("7 - Pesquisar por carga")
    print("8 - Alterar caminhão")
    print("9 - Remover caminhão")
    print("10 - Estatísticas")
    print("0 - Sair")
    print()

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_caminhao()

    elif opcao == "2":
        listar_caminhoes()

    elif opcao == "3":
        procurar_placa()

    elif opcao == "4":
        procurar_motorista()

    elif opcao == "5":
        procurar_cidade()

    elif opcao == "6":
        procurar_estado()

    elif opcao == "7":
        procurar_carga()

    elif opcao == "8":
        alterar_caminhao()

    elif opcao == "9":
        remover_caminhao()

    elif opcao == "10":
        estatisticas()

    elif opcao == "0":
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida.")

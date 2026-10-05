frota = []


def normalizar(texto):
    return texto.strip().lower()


def ler_texto(mensagem):
    while True:
        texto = input(mensagem).strip()

        if texto == "":
            print("Erro: o campo não pode ficar vazio.")
        else:
            return texto


def ler_ano():
    while True:
        try:
            ano = int(input("Ano do caminhão: "))

            if ano <= 0:
                print("Erro: digite um ano válido.")
            else:
                return ano

        except ValueError:
            print("Erro: digite apenas números para o ano.")


def normalizar_estado(estado):
    estado = normalizar(estado)

    if estado == "sao paulo" or estado == "sp":
        return "SP"

    elif estado == "parana" or estado == "pr":
        return "PR"

    elif estado == "minas gerais" or estado == "mg":
        return "MG"

    elif estado == "rio de janeiro" or estado == "rj":
        return "RJ"

    elif estado == "santa catarina" or estado == "sc":
        return "SC"

    elif estado == "rio grande do sul" or estado == "rs":
        return "RS"

    elif estado == "bahia" or estado == "ba":
        return "BA"

    elif estado == "goias" or estado == "go":
        return "GO"

    else:
        return ""


def ler_estado():
    while True:
        estado = input("Digite o estado: ")

        estado = normalizar_estado(estado)

        if estado == "":
            print("Erro: estado inválido.")
            print("Digite uma sigla ou o nome completo do estado.")
        else:
            return estado


def ler_placa():
    while True:
        placa = input("Digite a placa: ")
        placa = placa.strip().upper()

        if placa == "":
            print("Erro: a placa não pode ficar vazia.")

        elif len(placa) < 7:
            print("Erro: digite uma placa válida.")

        else:
            return placa


def mostrar_caminhao(caminhao):
    print("Placa:", caminhao["placa"])
    print("Modelo:", caminhao["modelo"])
    print("Motorista:", caminhao["motorista"])
    print("Cidade:", caminhao["cidade"])
    print("Estado:", caminhao["estado"])
    print("Carga:", caminhao["carga"])
    print("Ano:", caminhao["ano"])


def cadastrar_caminhao():
    print()
    print("CADASTRAR CAMINHÃO")

    placa = ler_placa()
    modelo = ler_texto("Digite o modelo: ")
    motorista = ler_texto("Digite o motorista: ")
    cidade = ler_texto("Digite a cidade: ")
    estado = ler_estado()
    carga = ler_texto("Qual o tipo de carga: ")
    ano = ler_ano()

    # Verificar se a placa já existe
    for caminhao in frota:
        if caminhao["placa"] == placa:
            print()
            print("Essa placa já está cadastrada.")
            return

    caminhao = {
        "placa": placa,
        "modelo": modelo,
        "motorista": motorista,
        "cidade": cidade,
        "estado": estado,
        "carga": carga,
        "ano": ano
    }

    frota.append(caminhao)

    print()
    print("Caminhão cadastrado com sucesso!")


def listar_caminhoes():
    print()
    print("LISTA DE CAMINHÕES")

    if len(frota) == 0:
        print("Nenhum caminhão cadastrado.")
        return

    for numero in range(len(frota)):
        caminhao = frota[numero]

        print()
        print("Caminhão", numero + 1)
        mostrar_caminhao(caminhao)


def procurar_placa():
    print()
    print("PESQUISAR PLACA")

    placa = ler_placa()

    encontrou = False

    for caminhao in frota:
        if caminhao["placa"] == placa:
            print()
            print("Caminhão encontrado!")
            mostrar_caminhao(caminhao)

            encontrou = True
            break

    if not encontrou:
        print("Nenhum caminhão encontrado.")


def procurar_motorista():
    print()
    print("PESQUISAR MOTORISTA")

    motorista = ler_texto("Digite o nome do motorista: ")
    motorista = normalizar(motorista)

    encontrou = False

    for caminhao in frota:
        if normalizar(caminhao["motorista"]) == motorista:
            print()
            print("Caminhão encontrado!")
            mostrar_caminhao(caminhao)

            encontrou = True

    if not encontrou:
        print("Nenhum caminhão encontrado para esse motorista.")


def procurar_cidade():
    print()
    print("PESQUISAR CIDADE")

    cidade = ler_texto("Digite o nome da cidade: ")
    cidade = normalizar(cidade)

    encontrou = False

    for caminhao in frota:
        if normalizar(caminhao["cidade"]) == cidade:
            print()
            print("Caminhão encontrado!")
            mostrar_caminhao(caminhao)

            encontrou = True

    if not encontrou:
        print("Nenhum caminhão encontrado nessa cidade.")


def procurar_estado():
    print()
    print("PESQUISAR ESTADO")

    estado = ler_estado()

    encontrou = False

    for caminhao in frota:
        if caminhao["estado"] == estado:
            print()
            print("Caminhão encontrado!")
            mostrar_caminhao(caminhao)

            encontrou = True

    if not encontrou:
        print("Nenhum caminhão encontrado nesse estado.")


def procurar_carga():
    print()
    print("PESQUISAR CARGA")

    carga = ler_texto("Digite o tipo de carga: ")
    carga = normalizar(carga)

    encontrou = False

    for caminhao in frota:
        if normalizar(caminhao["carga"]) == carga:
            print()
            print("Caminhão encontrado!")
            mostrar_caminhao(caminhao)

            encontrou = True

    if not encontrou:
        print("Nenhum caminhão encontrado com essa carga.")


def alterar_caminhao():
    print()
    print("ALTERAR CAMINHÃO")

    placa = ler_placa()

    caminhao_encontrado = None

    for caminhao in frota:
        if caminhao["placa"] == placa:
            caminhao_encontrado = caminhao
            break

    if caminhao_encontrado is None:
        print("Nenhum caminhão encontrado.")
        return

    print()
    print("Caminhão encontrado!")
    mostrar_caminhao(caminhao_encontrado)

    print()
    print("Deixe o campo vazio para não alterar.")

    novo_modelo = input("Novo modelo: ").strip()
    novo_motorista = input("Novo motorista: ").strip()
    nova_cidade = input("Nova cidade: ").strip()
    novo_estado = input("Novo estado: ").strip()
    nova_carga = input("Nova carga: ").strip()
    novo_ano = input("Novo ano: ").strip()

    if novo_modelo != "":
        caminhao_encontrado["modelo"] = novo_modelo

    if novo_motorista != "":
        caminhao_encontrado["motorista"] = novo_motorista

    if nova_cidade != "":
        caminhao_encontrado["cidade"] = nova_cidade

    if novo_estado != "":
        estado = normalizar_estado(novo_estado)

        if estado == "":
            print("Erro: estado inválido. O estado não foi alterado.")
        else:
            caminhao_encontrado["estado"] = estado

    if nova_carga != "":
        caminhao_encontrado["carga"] = nova_carga

    if novo_ano != "":
        try:
            novo_ano = int(novo_ano)

            if novo_ano <= 0:
                print("Erro: digite um ano válido.")
            else:
                caminhao_encontrado["ano"] = novo_ano

        except ValueError:
            print("Erro: digite apenas números para o ano.")

    print()
    print("Caminhão alterado com sucesso!")


def remover_caminhao():
    print()
    print("REMOVER CAMINHÃO")

    placa = ler_placa()

    caminhao_encontrado = None

    for caminhao in frota:
        if caminhao["placa"] == placa:
            caminhao_encontrado = caminhao
            break

    if caminhao_encontrado is None:
        print("Nenhum caminhão encontrado.")
        return

    print()
    print("Caminhão encontrado!")
    mostrar_caminhao(caminhao_encontrado)

    while True:
        confirmacao = input(
            "Deseja realmente remover? (S/N): "
        ).strip().upper()

        if confirmacao == "S":
            frota.remove(caminhao_encontrado)
            print("Caminhão removido com sucesso!")
            break

        elif confirmacao == "N":
            print("Remoção cancelada.")
            break

        else:
            print("Opção inválida.")
            print("Digite apenas S ou N.")


def estatisticas():
    print()
    print("ESTATÍSTICAS DA FROTA")

    if len(frota) == 0:
        print("Nenhum caminhão cadastrado.")
        return

    total = len(frota)

    quantidade_sp = 0
    quantidade_pr = 0
    quantidade_mg = 0
    quantidade_rj = 0
    outros = 0

    for caminhao in frota:
        estado = caminhao["estado"]

        if estado == "SP":
            quantidade_sp += 1

        elif estado == "PR":
            quantidade_pr += 1

        elif estado == "MG":
            quantidade_mg += 1

        elif estado == "RJ":
            quantidade_rj += 1

        else:
            outros += 1

    print("Total de caminhões:", total)
    print("Caminhões de SP:", quantidade_sp)
    print("Caminhões de PR:", quantidade_pr)
    print("Caminhões de MG:", quantidade_mg)
    print("Caminhões de RJ:", quantidade_rj)
    print("Caminhões de outros estados:", outros)

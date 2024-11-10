from Operations import (Modulo, ProdutoVetorial, ProdutoEscalar,
                        Angulo, Ortogonalizade)


def inicial():
    print("\n\n--- Menu ---")
    print("1. inserir novos valores")
    print("2. Listar vetores")
    print("3. selecionar vetores")
    print("4. Limpar seleção de vetores")
    print("5. selecionar operações")
    print("6. Sair \n\n")


def operacoes(selecionados: list):
    print("\n\n--- Menu ---")
    print("1. Calcular Módulo")
    print("2. Calcular Produto Escalar")
    print("3. Verficar Ortogonalidade")
    print("4. Calcular Ângulo entre Vetores")
    print("5. Calcular Produto Vetorial")
    print("6. Sair \n\n")
    opt = int(input("insira o número da operação: "))

    match opt:
        case 1:
            for x in selecionados:
                print("resultado " + str(Modulo(x)))
        case 2:
            x = ProdutoEscalar(selecionados[0], selecionados[1])
            print("resultado: " + str(x) + "\n")
        case 3:
            x = Ortogonalizade(selecionados[0], selecionados[1])
        case 4:
            x = Angulo(selecionados[0], selecionados[1])
        case 5:
            x = ProdutoVetorial(selecionados[0], selecionados[1])
        case 6:
            pass

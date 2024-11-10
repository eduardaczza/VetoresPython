from Menu import inicial, operacoes
from Vetor import Vetor
vetores = []
selecionados = []


def main():
    rodando = True
    global selecionados
    while (rodando):
        inicial()
        opt = int(input("insira ovalor da operação desejada \n"))
        match opt:
            case 1:
                print("Insira os valores do Vetor: ")
                vetores.append(Vetor.inserirVetor())
                continue
            case 2:
                print("Lista dos vetores: \n")
                Vetor.printMultiplosVetores(Vetor, vetores)
            case 3:
                vetorSelecionado = int(Vetor.selecionarVetores())
                if len(selecionados) < 2:
                    selecionados.append(vetores[vetorSelecionado-1])
                else:
                    print("Número máximo de vetores selecinados \n")
            case 4:
                selecionados = []
            case 5:
                operacoes(selecionados)
            case 6:
                rodando = False


if __name__ == "__main__":
    main()

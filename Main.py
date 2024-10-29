from .Menu import inicial, operacoes
from .Vetor import Vetor
from .Operations import Operar
vetores = []
selecionados = []


def main():
    op = 0
    while (op != 4):
        op = inicial()
        match op:
            case 1:
                Vetor.inserirVetor(vetores)
            case 2:
                Vetor.printMultiplosVetores(Vetor, vetores)
            case 3:
                Vetor.printMultiplosVetores(Vetor, vetores)
                operacao = operacoes()
                Operar(operacao, selecionados)


if __name__ == "__main__":
    main()

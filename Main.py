from Menu import inicial, operacoes
from Vetor import Vetor
vetores = []
selecionados = []

    # Função principal para rodar o programa
def main():
    rodando = True
    global selecionados
    # Loop principal para controlar a execução do programa
    while (rodando):
        inicial()
        opt = int(input("insira ovalor da operação desejada \n"))
        match opt:
            case 1:
                print("Insira os valores do Vetor: ")
                # Chama o método estático para inserir um vetor e adiciona à lista de vetores
                vetores.append(Vetor.inserirVetor())
                continue
            case 2:
                # Se o vetor existir é chamado o método para imprimir os vetores na lista 'vetores' 
                print("Lista dos vetores: \n")
                Vetor.printMultiplosVetores(Vetor, vetores)
            case 3:
                 # Caso o usuário escolha selecionar um vetor
                vetorSelecionado = int(Vetor.selecionarVetores())
                # Verifica se dois vteores foram selecionados  e adiciona a lista de seleção
                if len(selecionados) < 2:
                    selecionados.append(vetores[vetorSelecionado-1])
                else:
                    print("Número máximo de vetores selecinados \n")
            case 4:
                # Limpa a lista selecionada e permite uma nova seleçaõ
                selecionados = []
            case 5:
                # Caso os vetores selecionados sejam escolhidos permite que a lista seja passada com os vetores selecionados 
                operacoes(selecionados)
            case 6:
                rodando = False


if __name__ == "__main__":
    main()

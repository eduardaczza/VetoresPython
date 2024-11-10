class Vetor:
    #  Classe que define a representação de um vetor de três dimensões 

    # Construtor para inicializar as coordenadas x, y, e z do vetor
    def __init__(self, x: int, y: int, z: int):
        self.x = x
        self.y = y
        self.z = z

    #  Método para inserir um vetor com valores dados pelo usuário
    def inserirVetor():
        x = input("adicione o valor de X\n")
        y = input("adicione o valor de Y\n")
        z = input("adicione o valor de Z\n")
        vetor = Vetor(x, y, z)
        print("vetor adicionado com sucesso \n\n")
        return vetor

    # Método para imprimir um vetor com um índice fornecido
    def printVetor(self, index):
        print(str(index)+". "+"("+self.x+", "+self.y+", "+self.z+")\n")

    # Método para imprimir múltiplos vetores em uma lista
    def printMultiplosVetores(self, listaVetores: list):
        for idx, x in enumerate(listaVetores):
            self.printVetor(x, idx+1)

    # Método para selecionar um vetor com base em um índice fornecido pelo usuário
    def selecionarVetores():
        selectIndex = input("Digite o número do vetor que deseja selecionar: ")
        return selectIndex

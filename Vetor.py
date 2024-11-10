class Vetor:
    def __init__(self, x: int, y: int, z: int):
        self.x = x
        self.y = y
        self.z = z

    def inserirVetor():
        x = input("adicione o valor de X\n")
        y = input("adicione o valor de Y\n")
        z = input("adicione o valor de Z\n")
        vetor = Vetor(x, y, z)
        print("vetor adicionado com sucesso \n\n")
        return vetor

    def printVetor(self, index):
        print(str(index)+". "+"("+self.x+", "+self.y+", "+self.z+")\n")

    def printMultiplosVetores(self, listaVetores: list):
        for idx, x in enumerate(listaVetores):
            self.printVetor(x, idx+1)

    def selecionarVetores():
        selectIndex = input("Digite o número do vetor que deseja selecionar: ")
        return selectIndex

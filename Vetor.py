class Vetor:
    def __init__(self, x: int, y: int, z: int):
        self.x = x
        self.y = y
        self.z = z

    def inserirVetor(vetores: list):
        if len(vetores) > 3:
            print("operação invalida, limite vetores atingido")
            return
        x = input("adicione o primeiro valor")
        y = input("adicione o  valor")
        z = input("adicione o primeiro valor")
        vetor = Vetor(x, y, z)
        vetores.append(vetor)
        print("vetor adicionado com sucesso")
        return

    def printVetor(self, index):
        print(index+". "+"("+self.x+", "+self.y+", "+self.z+")")

    def printMultiplosVetores(self, listaVetores: list):
        for idx, x in enumerate(listaVetores):
            self.printVetor(x, idx+1)


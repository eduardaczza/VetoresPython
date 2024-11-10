import math
from Vetor import Vetor


# Calcula o módulo do vetor inserido na função
def Modulo(vetor: Vetor):
    print("")
    math.sqrt(math.pow(vetor.x, 2)+math.pow(vetor.y, 2)+math.pow(vetor.z, 2))


# Calcula o ângulo entre 2 vetores
def Angulo(vetor1: Vetor, vetor2: Vetor):
    prodInterno = (vetor1.x*vetor2.x) + \
        (vetor1.y*vetor2.y) + (vetor1.z*vetor2.z)
    modulov1 = Modulo(vetor1)
    modulov2 = Modulo(vetor2)
    cosPhi = prodInterno/(modulov1*modulov2)

    res = math.acos(cosPhi) * (180/math.pi)
    return res


def ProdutoEscalar(vetor1: Vetor, vetor2: Vetor):
    res = (vetor1.x*vetor2.x)+(vetor1.x*vetor2.x)+(vetor1.x*vetor2.x)
    return res

# https://pt.khanacademy.org/math/multivariable-calculus/thinking-about-multivariable-function/x786f2022:vectors-and-matrices/a/cross-products-mvc
# fonte do cálculo


def ProdutoVetorial(vetor1: Vetor, vetor2: Vetor):
    resX = (vetor1.y*vetor2.z)-(vetor1.z*vetor2.y)
    resY = (vetor1.z*vetor2.x)-(vetor1.x*vetor2.y)
    resZ = (vetor1.x*vetor2.y)-(vetor1.y*vetor2.x)

    resVetor = Vetor(resX, resY, resZ)
    return resVetor


def Ortogonalizade(vetor1: Vetor, vetor2: Vetor):
    if ProdutoEscalar(vetor1, vetor2) == 0:
        return True
    else:
        return False

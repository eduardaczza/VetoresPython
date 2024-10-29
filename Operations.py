import math


def Operar(op, listaVetores):
    match op:
        # mod operation
        #  Math.sqrt(Math.pow(x, 2) + Math.pow(y, 2) + Math.pow(z, 2));
        case 1:
            for x in listaVetores:
                math.sqrt(math.pow(x.x, 2)+math.pow(x.y, 2)+math.pow(x.z, 2))

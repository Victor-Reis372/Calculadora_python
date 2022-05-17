n1 = int(input("Digite o primeiro numero :"))
n2 = int(input("Digite o segundo numero  :"))

caso = int(input("Soma = 1 \nSubtração = 2 \nDivisão = 3 \nMultiplicação = 4 \nPotenciação = 5 \nDigite sua operação:"))

while caso < 1 or caso > 5:
    caso = int(input("Digite um numero entre 1 e 5 :"))


def soma(v1, v2):
    return v1+v2


def sub(v1, v2):
    return v1-v2


def div(v1, v2):
    return v1/v2


def mult(v1, v2):
    return v1*v2


def pot(v1, v2):
    return v1**v2


match caso:
    case 1: print(soma(n1, n2))
    case 2: print(sub(n1, n2))
    case 3: print(div(n1, n2))
    case 4: print(mult(n1, n2))
    case 5: print(pot(n1, n2))

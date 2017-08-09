__author__ = 'fhca'

from math import inf  # aprox 1e308

arbol1 = [[[8], [12], [16]], [[6], [9], [13]], [[10], [9], [7]]]

arbol2 = [[[[[10], [100]], [[5]]], [[-10]]], [[[[7], [5]], [[-100]]], [[[-7], [-5]]]]]

arbol3 = [[[3], [-1], [-4]], [[-2], [0], [-3]], [[2], [4], [1]]]

arbol4 = [[[[[5], [6]], [[7], [4], [5]]], [[[3]]]], [[[[6]], [[6], [9]]], [[[7]]]], [[[[5]]], [[[[9], [8]], [[6]]]]]]

def movimientos_posibles(estado):
    return estado

def estado_terminal(estado):
    return isinstance(estado, int)

def evaluación(estado):
    return estado

def aplicar(mov, estado):
    return mov

def MiniMax(estado):
    max = -inf
    for mov in movimientos_posibles(estado):
        max_actual = valorMin(aplicar(mov, estado))
        if max_actual > max:
            max = max_actual
            mejor_mov = mov
    return max, mejor_mov

def valorMax(estado):
    if estado_terminal(estado):
        return evaluación(estado)
    else:
        valor_max = -inf
        for mov in movimientos_posibles(estado):
            valor_max = max(valor_max, valorMin(aplicar(mov, estado)))
        return valor_max

def valorMin(estado):
    if estado_terminal(estado):
        return evaluación(estado)
    else:
        valor_min = +inf
        for mov in movimientos_posibles(estado):
            valor_min = min(valor_min, valorMax(aplicar(mov, estado)))
        return valor_min


print("MiniMax=", MiniMax(arbol2))

def minimax(node, depth, maxPlayer):
    if depth == 0 or estado_terminal(node):
        return evaluación(node)
    if maxPlayer:
        bestValue = -inf
        for child in node:
            val = minimax(child, depth - 1, False)
            bestValue = max(bestValue, val)
        return bestValue
    else:
        bestValue = +inf
        for child in node:
            val = minimax(child, depth - 1, True)
            bestValue = min(bestValue, val)
        return bestValue

print("uno=", MiniMax(arbol1))
print("minimax=", minimax(arbol2, 5, True))

print("tablah=", minimax(arbol3, 3, True))

print("MMa4=", MiniMax(arbol4))
print("a4=", minimax(arbol4, 7, True))
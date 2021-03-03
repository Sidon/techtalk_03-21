"""
Cálculo de juros simples
"""


##
# Calcula o juros simples do capital informado
# Argumentos:
#    c = Capital
#    i = Taxa de juros
#    n = Número de períodos
#
#    Exemplo de uso:
#       ``juros_calculado = juros_simples(500, 3, 5)``
#       print(juros_calculado)
##
def juros_simples1(c: float, i: float, n: int):
    return c*i*n


def juros_simples(c: float, i: float, n: int):
    """
    Calcula o juros simples do capital informado

    Argumentos:
    
        c = Capital
        i = Taxa de juros
        n = Número de períodos

        Exemplo de uso:

        juros_calculado = juros_simples(500, 3, 5)
        print(juros_calculado)

    """    
    
    return c*i*n


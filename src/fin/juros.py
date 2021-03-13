from .mymath import Calc



def juros_simples(c: float, i: float, n: int) -> float:
    """
    Calculo de juros simples.

    Calcula os juros simples do capital informado

    :param c: Capital sobre o qual será feito o cálculo
    :type c: float
    :param i: Taxa de juros por período
    :type i: float
    :param n: Número de períodos
    :type n: int
    :return: Valor dos juros calculado sobre o capital, no perído informado.
    :rtype: float
    """ 
    return c*i*n


def juros_compostos(c: float, cf: float, n: int) -> float:
    """
    Cálculo de juros compostos

    Calcula os juros compostos de um capital sobre o valor final.

    :param c: Capital inicial
    :type c: float
    :param cf: Capital atualizado no final dos períodos (Valor final)
    :type cf: float
    :param n: Número de perídos
    :type n: int
    :return: Taxa de juros aplicada
    :rtype: float
    """
    
    return (cf/c)**(1/3.) -1 
    
    

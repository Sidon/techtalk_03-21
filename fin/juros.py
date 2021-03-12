from .mymath import Calc



def juros_simples(c: float, i: float, n: int) -> float:
    """
    Calcula o juros simples do capital informado.

    :param c: (float) Capital  
    :param i: (float) Taxa de juros por período
    :param n: (int) Número de períodos 
    
    :returns (float): juros calculado sobre o capital no período informado 

    :Examplo de uso:
    
    .. code-block:: python
    capital = 100
    taxa = 10
    periodos = 3
    juros = juros_simples2(capital, taxa, periodos)
    """
    
    return c*i*n


def vf_juros_compostos(c, i, n) -> float:
    """
    Calcula o valor futuro de um capital no regime de juros compostos

    :param c: Valor atual do capital
    :type c: float
    :param i: Taxa de juros a ser aplicada
    :type i: float
    :param n: Numero de períodos
    :type n: integer
    :return: Valor futuro do capital
    :rtype: float
    """
    
    return c * (1+i)**n
    
    

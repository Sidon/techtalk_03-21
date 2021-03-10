"""
Calculo de juros simples
"""


def juros_simples1(c: float, i: float, n: int) -> float:
    """
    Calcula o juros simples do capital informado

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


##
# Calcula o juros simples do capital informado
# Argumentos:
#    c = Capital
#    i = Taxa de juros
#    n = Numero de periodos
#
#    Exemplo de uso:
#       ``juros_calculado = juros_simples(500, 3, 5)``
#       print(juros_calculado)
##
def juros_simples2(c: float, i: float, n: int):
    return c*i*n




def test(a,b,c):
    """
    Função teste bla bla bla blabla bla

    :param a: Capital a ser calculoado o juro
    :type a: float
    :param b: Taxa a ser aplicada
    :type b: fCaraloat
    :param c: Tempo de maturação
    :type c: int
    """
    
    return a


class A:
    """
    Classe de teste para o docstring
    """
    active: bool
    """
    Identifica se o atribuo foi documentado
    """
    def f1():
        """
        Document f1
        """
        pass

def f10(a: A):
    """
    recebe a classe A

    Args:
        a (A): Parametro classe
    """


def f2():
    f10()


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
    
    
def vf_juros_compostos2(c: float, i: float, n: int) -> float:
    """
    Calcula o valor futuro de um capital no regime de juros compostos
 
    Parametros:
        
    - c (float): Valor atual do capital
    - i (float): Taxa de juros a ser aplicada
    - n (int): Número de períodos
   
    Returns 
    ~~~~~~~
    - Valor futuro do capital informado  
    """
    
    return c * (1+i)**n


def f1(p1, p2, p3) -> float:
    """
    [summary]

    :param p1: [description]
    :type p1: [type]
    :param p2: [description]
    :type p2: [type]
    :param p3: [description]
    :type p3: [type]
    :return: [description]
    :rtype: float
    """
    
def f1(p1, p2, p3) -> float:
    """
    [summary]

    Args:
        p1 ([type]): [description]
        p2 ([type]): [description]
        p3 ([type]): [description]

    Returns:
        float: [description]
    """
        

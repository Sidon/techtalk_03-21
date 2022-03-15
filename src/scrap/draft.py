"""
Módulo para testes.

Tem como objetivo apenas demonstrar testes em "hands-on" e/ou aumentar o volume.
"""
    
    
class Calc:
    """
    Classe para operações aritméticas.
    
    Apenas para "encher linguiça", voce pode ver algo mais nesse link -> :mod:`src.fin.juros`

    Métodos
    --------
    - add
    - times

    :return: [description]
    :rtype: [type]
    """
    
    @staticmethod
    def add(n: float, m: float) -> float:
        """
        Realiza a adição de dois números do tipo float.

        Tem como objetivo apenas a demonstração da capacidade de referencia cruzada de reStructured text.

        :param n: Primeiro membro da operação de adição
        :type n: float
        :param m: Segundo membro da operação de adição
        :type m: float
        :return: Resultado da operação
        :rtype: float
        """
        return n+m 
    
    @staticmethod
    def times(n: float, m: float) -> float:
        """
        Realiza a multiplicação entre dois número do tipo float.

        Tem como objetivo apenas a demonstração da capacidade de refrencia cruzada de reStructured text.

        :param n: Primeiro membro da operação
        :type n: float
        :param m: Segundo membro da operação de multiplicação
        :type m: float
        :return: Resultado da operaçãoCode is more often read than written
        :rtype: float
        """ 
        
        return m*n



"""
Calculo de juros simples.
Calcula os juros simples do capital informado.
O parametro c refere-se ao capital, i é a taxa de juros do período e n é o número de períodos.
"""
def j1(c: float, i: float, n: int) -> float:
    return c * i * n


def j2(c: float, i: float, n: int) -> float:
    """
    Calculo de juros simples.

    Calcula os juros simples do capital informado.

    :param c: Capital sobre o qual será feito o cálculo.
    :type c: float
    :param i: Taxa de juros por período.
    :type i: float
    :param n: Número de períodos.
    :type n: int
    :return: Valor dos juros calculado sobre o capital, no período informado.
    :rtype: float
    """ 
    return c*i*n


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

        Tem como objetivo apenas a demonstração da capacidade de refrencia cruzada de reStructured text.

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
        :return: Resultado da operação
        :rtype: float
        """ 
        
        return m*n

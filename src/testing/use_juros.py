from ..fin.juros import juros_simples as js

def use_js():
    """
    Teste no uso dadiretiva :func:.

    Essa função utiliza a função juros simples :func:`src.fin.juros.juros_simples` do pacote fin.
    """
    juros = js(300, .10, 6)    

    return juros
    

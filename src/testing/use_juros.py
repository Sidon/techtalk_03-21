from ..fin import juros


def use_js():
    """
    Teste no uso da diretiva :func:.

    Essa função utiliza a função juros simples :func:`src.fin.juros.juros_simples` do pacote fin.
    """
    jrs = js(300, .10, 6)

    return jrs


juros.juros_compostos()
juros.juros_simples()

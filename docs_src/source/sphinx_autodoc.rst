.. _sphinx-long:

=======
Sphinx
=======

"Sphinx é um gerador de documentação ou uma ferramenta que traduz um conjunto de
arquivos fonte de texto simples em vários formatos de saída, produzindo 
automaticamente referências cruzadas, índices, etc. Ou seja, se você tiver um 
diretório contendo um monte de /usage/reestruturedtext/index ou Markdown, o 
Sphinx pode gerar uma série de arquivos HTML, um arquivo PDF (via LaTeX), 
páginas de manual e muito mais."

Instale o Sphinx: https://pypi.org/project/Sphinx/#files

*****************************
Inicializando a configuração
*****************************
No diretório raiz do seu projeto, execute **sphinx-quickstart** para inicializar 
o diretório de origem do sphinx para criar uma configuração padrão. A execução 
desse comando solicitará que você preencha algumas propriedades de configuração 
básicas, como se deseja criar diretórios de origem e de compilação separados, o 
nome do projeto, o nome do autor e a versão do projeto.

::

    $ sphinx-quickstart <path/to/doc>

*****************************************
Estrutura criada pelo sphinx-quickstart:
*****************************************

:: 

    doc
    ├── build
    ├── make.bat
    ├── Makefile
    └── source
        ├── conf.py
        ├── index.rst
        ├── _static
        └── _templates  


Como o path informado na execução do sphinx-quickstart foi ``./doc``, o quickstart
criou a pasta doc como raiz da documentação e separou as pastas buid e source, porque
essa opção foi selecionada. O arquivo Makefile serve para gerar automaticamente os 
arquivos html, na pasta source foi gerado os arquivos conf.py e index.rst, o primeiro
tem como objetivo a configuração e o segundo será explicado na próxima secção.

**************************
Extendendo a configuração
**************************
Versões anteriores do sphinx-quickstart solicitavam que o usuário fornecesse uma 
série de informações para construir o arquivo **conf.py**, a versão atual (na 
data da escrita desse texto, 3.5.2) é bem minimalista, exige que os parametros
sejam enviados na chamada ou voce terá que alterar o arquivo **conf.py** após a 
a sua exeção, um exemplo do como o arquivo deveria ficar para gerar documentação 
para o python:

::

    import os
    import sys
    sys.path.insert(0, os.path.abspath('../src'))

    project = 'Techtalks Docstrings'
    copyright = '2021, gb.lab'
    author = 'Sidon'

    release = '1.0'

    extensions = [
        'sphinx.ext.autodoc', 
        'sphinx.ext.viewcode',
        'sphinx_rtd_theme'
    ]

    # -- Options for HTML output 
    templates_path = ['_templates']
    language = 'pt_BR'
    html_theme = "sphinx_rtd_theme"
    master_doc = 'index
    pygments_style = None
    html_static_path = ['_static']


********************
O arquivo index.rst
********************

index.rst é o documento mestre que tem como função principal servir de página de 
boas-vindas, bem como conter a documentação raiz da estrutura “sumário” ou (toctree). 
Isso é um dos princípios que Sphinx usa para adicionar reStructuredText para conectar 
múltiplos arquivos em uma hierarquia simples de documentos.

Diretivas reStructuredText
==========================
Diretivas podem conter argumentos, opções e Conteúdos.
Argumentos são fornecidos diretamente após duplo dois pontos seguidos do nome da diretiva. 

Cada diretiva decide se existem e quantos são os argumentos.
Opções são fornecidas após os argumentos, na forma de “lista de campos”. Como em maxdepth 
que é uma opção da diretiva toctree.

Conteúdo segue opções ou argumentos após uma linha em branco. Cada diretiva decide como 
permite conteúdo e como tratá-lo.


A diretiva toctree
==================
| **toctree** é uma diretiva reStructuredText, inicialmente ela deve se parecer com:

::

    .. toctree::
    :maxdepth: 2
    :caption: Contents:

Você adiciona documentos listando-os no content da diretiva:

::

    .. toctree::
    :maxdepth: 2
    :caption: Contents:

    usage/installation
    usage/quickstart
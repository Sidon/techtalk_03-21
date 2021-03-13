
=====
TL;DR 
=====

*****************
Instale o sphinx
*****************
::

    pip install Sphinx

**************************
Execute sphinx-quickstart
**************************
::

    sphinx-quickstart ./docs_src

    $ tree

    docs_src
    ├── build
    ├── make.bat
    ├── Makefile
    └── source
        ├── conf.py
        ├── index.rst
        ├── _static
        └── _templates  


***************************
Atualize o arquivo conf.py
***************************
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

*****************************
Customize o arquivo index.rst
*****************************
::

    Welcome to Techtalks docstrings's documentation!
    ================================================

        .. toctree::
        :maxdepth: 2
        :caption: Contents:

        source/modules.rst
        source/intro.rst
        source/sphinx_autodoc.rst
        source/tldr.rst

        Indices and tables
        ==================

        * :ref:`genindex`
        * :ref:`modindex`
        * :ref:`search`

Não esqueça de mover os arquivos adicionais para a pasta source, nesse exemplo
source/intro.rst, source/sphinx_autodoc.rst e esse proprio arquivo. modules.rst
será gerado pelo comando sphinx-apidoc adicionado no arquivo Makefile.


*****************************
Customize o arquivo Makefile
*****************************
::

    SPHINXOPTS    ?= -a
    SPHINXBUILD   ?= sphinx-build
    SOURCEDIR     = .
    BUILDDIR      = _build

    HTMLDIR       = _build/html
    DOCSDIR       = ../docs

    # Put it first so that "make" without argument is like "make help".
    help:
        @$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

    .PHONY: help Makefile

    # Catch-all target: route all unknown targets to Sphinx using the new
    # "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
    %: Makefile
        sphinx-apidoc -f --ext-autodoc -o source ../src/fin
        @$(SPHINXBUILD) -M $@  "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
        cp -rf $(HTMLDIR)/* $(DOCSDIR)

******************************
Configure docs local/github
******************************

Local
-----
::

    on  master branch
    $ makedir <project_root>/docs

Github
-------
::
    Na pagina do projeto 
    settings/github pages/

***************
Execute o make
***************
::

    make html

****************
Atualize o repo
****************
::

    $ git add -u 
    $ git commit -m 'Update tldr and html' 
    $ git push
    
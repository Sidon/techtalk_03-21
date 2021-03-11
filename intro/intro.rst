==========
Docstrings
==========
Em programação, uma docstring é uma string literal especificada no código fonte, usada como um 
comentário, para documentar um segmento específico de código.

Linguagens que suportam dosctrings incluem Python, Lisp, Elixir, Clojure, Gherkin, 
Julia and Haskell.
    
Wikipedia

----------------------------
Convenções para  Docstring:
----------------------------
* A primeira linha deve ser uma breve descrição.

* Não escreva o nome do objeto. Se houver mais linhas na string de documentação, a segunda linha deve ficar em branco.

* As linhas a seguir devem ser um ou mais parágrafos que descrevem as convenções de chamada do objeto, seus efeitos colaterais, etc.

-----------------
Python docstring 
-----------------
Em python, uma docstring fornece uma maneira conveniente de associar a documentação aos módulos, 
funções métodos e classes. Ao contrário dos comentários convencionais do código-fonte, 
**uma docstring deve descrever o que a função faz, e não como.**

PEP 257
=======
Uma docstring é uma string literal que ocorre como a primeira instrução em uma definição de módulo, 
função, classe ou método. Tal docstring torna-se o atributo especial ```__doc__``` desse objeto.

Módulos
-------
Todos os módulos normalmente devem ter docstrings, e todas as funções e classes exportadas por um 
módulo também devem ter docstrings. 

Métodos públicos
----------------
Os métodos públicos (incluindo o construtor ```__init__``` ) 
também devem ter docstrings. 

Pacotes
-------
Um pacote pode ser documentado no docstring do módulo do 
arquivo ```_init__.py``` no diretório do pacote.

----------------
reStructuredText
----------------
reStructuredText é um sistema analisador e sintaxe de marcação de texto simples de fácil 
leitura, o que você vê é o que você obtém. É útil para, entre outros usos, documentação 
de programa em linha (como docstrings do Python).

O objetivo principal do reStructuredText é definir e implementar uma sintaxe de marcação 
para uso em docstrings Python e outros domínios de documentação.
| Site: https://docutils.sourceforge.io/rst.html

-------
Sphinx
-------
Sphinx é um gerador de documentação ou uma ferramenta que traduz um conjunto de arquivos 
fonte de texto simples em vários formatos de saída, produzindo automaticamente referências cruzadas, 
índices, etc.

Muito do poder do Sphinx vem da riqueza de seu formato de marcação de texto simples padrão, 
reStructuredText.
(https://www.sphinx-doc.org/pt_BR/master/usage/quickstart.html)


.. header::
 ###Section###


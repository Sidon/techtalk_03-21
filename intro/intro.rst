==========
Docstrings
==========
Em python, uma docstring fornece uma maneira conveniente de associar a documentação aos módulos, 
funções métodos e classes. Ao contrário dos comentários convencionais do código-fonte, 
**uma docstring deve descrever o que a função faz, e não como.**

    Em programação, uma docstring é uma string literal especificada no código fonte, usada como um 
    comentário, para documentar um segmento específico de código.

    Linguagens que suportam dosctrings incluem Python, Lisp, Elixir, Clojure, Gherkin, 
    Julia and Haskell.
    
    Wikipedia

Convenções para  Docstring:
===========================
A linha da string doc deve começar com uma letra maiúscula e terminar com um ponto. 
A primeira linha deve ser uma breve descrição.

Não escreva o nome do objeto. Se houver mais linhas na string de documentação, 
a segunda linha deve ficar em branco, separando visualmente o resumo do resto da descrição.

As linhas a seguir devem ser um ou mais parágrafos que descrevem as convenções de chamada 
do objeto, seus efeitos colaterais, etc.

reStructuredText
================
reStructuredText é um sistema analisador e sintaxe de marcação de texto simples de fácil 
leitura, o que você vê é o que você obtém. É útil para documentação de programa em linha 
(como docstrings do Python), para criar páginas da web simples rapidamente e para 
documentos autônomos. reStructuredText é projetado para extensibilidade para domínios de 
aplicativo específicos. O analisador reStructuredText é um componente do Docutils. 
reStructuredText é uma revisão e reinterpretação dos sistemas de marcação leve 
StructuredText e Setext.

O objetivo principal do reStructuredText é definir e implementar uma sintaxe de marcação 
para uso em docstrings Python e outros domínios de documentação, que seja legível e simples, 
mas poderosa o suficiente para uso não trivial. O objetivo pretendido da marcação é a 
conversão de documentos reStructuredText em formatos de dados estruturados úteis.
| Site: https://docutils.sourceforge.io/rst.html

Sphinx
======
Sphinx é um gerador de documentação ou uma ferramenta que traduz um conjunto de arquivos 
fonte de texto simples em vários formatos de saída, produzindo automaticamente referências cruzadas, 
índices, etc. Ou seja, se você tiver um diretório contendo uma grande quantidade de reStructuredText 
ou Markdown, o Sphinx pode gerar uma série de arquivos HTML, um arquivo PDF (via LaTeX), páginas de 
manual e muito mais. (https://www.sphinx-doc.org/pt_BR/master/usage/quickstart.html)

O Sphinx se concentra na documentação, em particular na documentação manuscrita; no entanto, o Sphinx 
também pode ser usado para gerar blogs, páginas iniciais e até livros. Muito do poder do Sphinx vem da 
riqueza de seu formato de marcação de texto simples padrão, reStructuredText, junto com seus recursos 
de extensibilidade significativos.

.. footer::
 ###Page###

.. header::
 ###Title### | Esta apresentação foi feita com docstrings :-).    

 

Docstrings
==========
Em python, uma docstring fornece uma maneira conveniente de associar a documentação aos módulos, 
funções métodos e classes. Ao contrário dos comentários convencionais do código-fonte, 
**uma docstring deve descrever o que a função faz, e não como.**

    Em programação, uma docstring é uma string literal especificada no código fonte, usada como um 
    comentário, para documentar um segmento específico de código.

    Linguagens que suportam dosctrings incluem Python, Lisp, Elixir, Clojure, Gherkin, 
    Julia and Haskell.
    
    -- Wikipedia

Convenções para  Docstring:
---------------------------
A linha da string doc deve começar com uma letra maiúscula e terminar com um ponto. 
A primeira linha deve ser uma breve descrição.

Não escreva o nome do objeto. Se houver mais linhas na string de documentação, 
a segunda linha deve ficar em branco, separando visualmente o resumo do resto da descrição.

As linhas a seguir devem ser um ou mais parágrafos que descrevem as convenções de chamada 
do objeto, seus efeitos colaterais, etc.

reStructuredText
================
É um formato de arquivo para dados textuais usado principalmente na comunidade da linguagem 
de programação Python para documentação técnica.
| Site: https://docutils.sourceforge.io/rst.html

Sphinx
======
Sphinx é um gerador de documentação ou uma ferramenta que traduz um conjunto de arquivos 
fonte de texto simples em vários formatos de saída, produzindo automaticamente referências cruzadas, 
índices, etc. Ou seja, se você tiver um diretório contendo um monte de /usage/reestruturedtext/index 
ou Markdown, o Sphinx pode gerar uma série de arquivos HTML, um arquivo PDF (via LaTeX), páginas de 
manual e muito mais. (https://www.sphinx-doc.org/pt_BR/master/usage/quickstart.html)


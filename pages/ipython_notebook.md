title: ipython notebook study notes
date: 2015-04-18
tags: [python, ipython_notebook]
published: 2015-04-18 
summary: Those are my study notes on ipython notebook. 
public: no


https://github.com/tiagoprn/pyconnz2013talk

$ ipython notebook --pylab inline
(--pylab: inicia a python matplotlib e o numpy
inline: the graphs appear on the notebook)

Ao abrir, mostra os notebooks que estão no diretório onde vc está.

Um notebook consiste de "cells". Cells podem ser de diferentes "types".

Notes podem ser escritas em markdown e plain text.

Pode ser usado quando você quer fazer anotações sobre o que você está fazendo juntamente com o código que você está escrevendo. Pode ser um ambiente interativo, de experimentação e/ou demonstração.

Notebooks podem ser compartilhados. Podem ser "hospedados" na internet read-only.

No menu help:
uma "?" mostra as docstrings de um métoto
duas "??" mostram o código de um método

Ipython magic methods:
    %timeit: mostra o tempo de execução de uma célula ou linha
        Ex.: %timeit [linha de código aqui]
    %pastebin: cria um gist com a célula ou linha
    %save: salva uma célula ou um range de células para um .py
    %load: carrega um arquivo em uma célula
    %run: roda um script python. Todos os símbolos do script serão carregados no namespace da sessão atual do ipython.

Poderoso se usado com o pandas.
    - pandas data structures:
        - series (array)
        - dataframe (table)
    - Strong Time-based indexing and dealing with date ranges
        dataframe.series.plot() : plota um gráfico dos dados
    - melhor usar datas UTC para padronizar as datas sem se preocupar com fusos horários.
    - convert pandas datetimes to python datetimes for interacting with matplotlib (plot the data)

    - dataset.describe(): sumário rápido dos dados

    - you can make a simple dataframe merging 2 or more series

    - dataframe.groupby('field').sum()

    - dataframes can be exported to: latex tables, csv, json, etc...

DOCKER IMAGE:
    docker pull ipython/scipyserver

    ENVIRONMENT VARIABLES:
        - PASSWORD

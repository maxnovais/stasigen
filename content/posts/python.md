title: python study notes
slug: python-study-notes
date: 2015-04-18
tags: [python, nose]
published: 2015-04-18
summary: My python study notes, for future reference.
public: yes

NOSE:

    Run a single test module:

        $ nosetests -s --ipdb -v [[script.py]]

        E.g.:

            $ cd /code/precifica/normalizer/tests && nosetests -s --ipdb -v main.py

    Run a single test method on a test module:

        $ nosetests -s --ipdb -v [[script.py]]:[[ClassName]].[[method_name]]

        E.g.:

            $ cd /code/precifica/normalizer/tests && nosetests -s --ipdb -v main.py:MainTestCase.test_generic_extractor_dict_generation

---

# compile_colors.py

''' Compile a list of all the different colors from the colors.csv
input file. We use the "set" python datatype to easily provide
this funcionality without adding duplicated values. '''

colors = set()
with open('colors.csv', 'r') as input_file:
    for record in input_file.readlines():
        expression = record.replace('\n', '').split('/')
        for line in expression:
            words = line.split(' ')
            for word in words:
                colors.add(word)
    print 'Total of unique words: {}'.format(len(colors))
    print 'UNIQUE WORDS:'
    print repr(colors)

# colors.csv
red / orange
white / black
black / orange
titanium
green
gloss
yellow
white / blue
black
azul
matt blk
white / green
white / anth
silver / anth
white
pink / silver
silver
white / red
branco/prata
verde claro/branco
rosa/roxo
laranja esc/azul esc
preto/laranja esc
laranja/azul
transparente
marrom cla/azul cla
marrom claro
laranja/verde cla
azul cla/roxo
azul
verde esc/verde cla
rosa/azul esc
laranja claro
branco/verde escuro
marrom cla/preto
verde/preto
azul/ouro
amarelo escuro
preto/rosa
verde esc/verde
cinza/cinza esc
vermelho/branco
cinza escuro
azul esc/azul cla
cinza/rosa
azul/azul esc
roxo/vermelho
azul/branco
cinza/vermelho
laranja esc/verde
cinza cla/rosa
rosa/rosa cla
roxo/marrom cla
cinza/preto
rosa esc/branco
marrom
azul esc/verde
vinho/azul escuro
azul cla/azul
vermelho/verde
rosa/preto
verde esc/marrom
vermelho/azul
branco/rosa esc
azul esc/amarelo
roxo/laranja
vermelho/cinza esc
vermelho/cinza
marrom/preto
amarelo/azul
cinza cla/azul
azul esc/marrom cla
cinza esc/verde
azul escuro/prata
nao se aplica
branco/verde cla
cinza/azul esc
rosa/cinza cla
laranja/rosa
laranja esc/preto
vinho/verde
ouro
marrom/branco
cinza/azul
rosa/cinza
vermelho/preto
rosa esc/cinza
rosa
azul esc/preto
branco/verde
rosa/azul
preto/laranja
roxo/roxo cla
branco/preto
roxo claro
roxo cla/laranja esc
marrom cla/marrom
roxo claro/branco
azul cla/rosa
azul/verde
marrom cla/azul
verde cla/verde esc
cinza cla/verde cla
vinho/branco
cinza escuro/branco
roxo esc/cinza cla
roxo
verde/vermelho
branco/vermelho
amarelo claro
verde claro
verde esc/rosa
ouro/verde cla
laranja/cinza cla
marrom/amarelo esc
cinza cla/verde
vinho/rosa
cinza/marrom
preto/amarelo
roxo escuro
rosa/prata
branco/azul
laranja
azul esc/vermelho
laranja/amarelo
azul/vermelho
verde cla/verde
rosa/verde cla
vinho/azul
laranja esc/cinz cla
amarelo/azul escuro
azul/amarelo
rosa/roxo cla
preto/marrom
branco/vinho
vermelho/azul esc
preto/roxo
marrom cla/laranja
preto/branco
verde cla/amarelo
cinza esc/verde cla
cinza esc/cinza
branco/roxo
verde cla/cinza esc
azul esc/azul
branco/azul esc
ouro/preto
amarelo/verde
salmao
verde/vinho
azul/cinza cla
bronze
branco/roxo escuro
roxo esc/verde
branco/laranja cla
azul esc/verde cla
azul esc/laranja
rosa esc/preto
verde cla/azul
cinza/roxo
prata
roxo esc/preto
cinza cla/branco
cinza cla/laranja
azul/verde cla
laranja/azul esc
rosa/laranja esc
cinza esc/rosa
branco/rosa cla
laranja/preto
laranja esc/branco
verde cla/laranja
branco/rosa
azul cla/branco
azul cla/azul esc
marrom esc/verde esc
azul cla/cinza
roxo cla/rosa
cinza escuro/preto
azul/rosa
preto/prata
cinza cla/preto
amarelo/rosa
cinza cla/cinza
marrom/vermelho
amarelo/cinza
azul esc/cinza cla
cinza esc/vinho
marrom cla/verde
cinza
cinza cla/cinza esc
verde/branco
laranja cla/lara esc
branco/cinza esc
amarelo/laranja
branco/amarelo
verde esc/amarelo
verde esc/branco
roxo esc/roxo cla
verde/cinza cla
preto/azul cla
azul escuro
cinza esc/azul cla
cinza/verde cla
laranja/branco
preto/azul esc
cinza esc/laranj cla
preto/rosa esc
verde/laranja
cinza escuro/amarelo
marrom/rosa
roxo claro/cinza
roxo/verde cla
azul/cinza
marrom cla/vermelho
verde esc/laranja
branco/marrom
cinza esc/vermelho
vinho
roxo/azul cla
vermelho/prata
azul cla/cinza cla
amarelo/preto
azul esc/cinza esc
verde/azul esc
laranja esc/azul
cinza esc/laranj esc
amarelo/roxo
vinho/preto
verde escuro
verde cla/azul esc
azul/marrom cla
marrom escuro
cinza cla/laranj esc
verde/azul
cinza/verde
amarelo/branco
branco/ouro
cinza claro
laranja escuro
verde/verde esc
rosa/verde
azul cla/verde
azul cla/amarelo
vinho/laranja esc
verde cla/azul cla
marrom claro/branco
branco
branco/cinza claro
preto/azul
preto/laranja cla
preto/verde escuro
azul esc/cinza
cinza cla/vermelho
azul/preto
amarelo/vermelho
azul cla/verde cla
laranja/marrom esc
laranja/azul claro
cinza cla/azul cla
cinza cla/roxo
azul esc/ouro
verde esc/azul esc
verde cla/rosa
rosa escuro
preto/ouro
preto/cinza
roxo cla/roxo
branco/marrom cla
marrom/marrom cla
preto/marrom cla
cinza/cinza cla
azul esc/vinho
preto/vermelho
azul/roxo
marrom/verde
amarelo
laranja/laranja cla
vermelho/azul cla
azul esc/roxo
laranja/roxo
cinza esc/laranja
cinza esc/cinza cla
roxo/branco
verde cla/roxo
amarelo esc/preto
vermelho/amarelo
marrom cla/rosa
preto/cinza claro
preto/cinza esc
cinza esc/azul
cinza/branco
rosa/branco
roxo/rosa
amarelo/verde cla
azul claro/preto
verde claro/preto
azul esc/roxo cla
roxo cla/cinza cla
azul esc/rosa
branco/laranja
azul/laranja
rosa/amarelo
verde esc/preto
laranja/cinza escuro
azul cla/cinza esc
cinza/laranja
verde esc/vermelho
roxo/preto
rosa claro
rosa/laranja
vermelho
rosa esc/rosa
azul esc/branco
rosa/ouro
verde cla/cinza cla
verde esc/ouro
branco/azul cla
preto
cinza/roxo esc
verde cla/vermelho
verde
preto/verde cla
verde/amarelo
azul claro
preto/verde
laranja/verde
branco/cinza

---

When to use @staticmethod and @classmethod:
    - I should use @classmethod when I want to act on various instances, at the class level. It can be used for a cache of all of the class instances, for example.

---

Em python, para fazer algo que usa muita memória usar menos devo transformar listas e outras estruturas em memória em geradores.

---



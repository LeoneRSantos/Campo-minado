from tkinter import *

from views.tela_do_jogo import TelaDoJogo

# O software deve mostrar todas as casas que continham bombas ao clicar em uma.

tela = Tk() 

def testar_bombas_descobertas_facil():
    tf = TelaDoJogo(8,8,10,tela)
    cont = 0

    for l in range(tf.linhas):
        for c in range(tf.colunas):
            if tf.casasRandomicas[l][c] == True:
                tf.matrizDoJogo[l][c]['text'] = 'B'
                cont +=1

    assert tf.bombas == cont

def testar_bombas_descobertas_intermediario():
    ti = TelaDoJogo(10,16,30,tela)
    cont = 0

    for l in range(ti.linhas):
        for c in range(ti.colunas):
            if ti.casasRandomicas[l][c] == True:
                ti.matrizDoJogo[l][c]['text'] = 'B'
                cont +=1

    assert ti.bombas == cont

def testar_bombas_descobertas_dificil():
    td = TelaDoJogo(24,24,100,tela)
    cont = 0

    for l in range(td.linhas):
        for c in range(td.colunas):
            if td.casasRandomicas[l][c] == True:
                td.matrizDoJogo[l][c]['text'] = 'B'
                cont +=1

    assert td.bombas == cont

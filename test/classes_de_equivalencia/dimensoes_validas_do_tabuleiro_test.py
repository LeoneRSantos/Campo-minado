from tkinter import Tk
from views.tela_do_jogo import TelaDoJogo

tela = Tk()

def testar_dimensoes_validas_de_tabuleiro_facil():
    tf = TelaDoJogo(8,8,10,tela)
    area = 0

    for l in range(tf.linhas):
        for c in range(tf.colunas):
            area += 1

    assert area == 64


def testar_dimensoes_validas_de_tabuleiro_intermediario():
    ti = TelaDoJogo(10,16,30,tela)
    area = 0

    for l in range(ti.linhas):
        for c in range(ti.colunas):
            area += 1

    assert area == 160

def testar_dimensoes_validas_de_tabuleiro_dificil():
    td = TelaDoJogo(24,24,100,tela)
    area = 0

    for l in range(td.linhas):
        for c in range(td.colunas):
            area += 1

    assert area == 576


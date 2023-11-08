from tkinter import Tk
from views.tela_do_jogo import TelaDoJogo

tela = Tk()


def testar_Se_Existe_bombas_Facil():

    t = TelaDoJogo(8, 8, 10, tela)
    qtdBombas = 0

    for l in range(t.linhas):
        for c in range(t.colunas):
            if t.casasRandomicas[l][c] == True:
                qtdBombas += 1

    assert qtdBombas > 0


def testar_Se_Existe_bombas_Intermediario():

    t = TelaDoJogo(10, 16, 30, tela)
    qtdBombas = 0

    for l in range(t.linhas):
        for c in range(t.colunas):
            if t.casasRandomicas[l][c] == True:
                qtdBombas += 1

    assert qtdBombas > 0


def testar_Se_Existe_bombas_Dificil():

    t = TelaDoJogo(24, 24, 100, tela)
    qtdBombas = 0

    for l in range(t.linhas):
        for c in range(t.colunas):
            if t.casasRandomicas[l][c] == True:
                qtdBombas += 1

    assert qtdBombas > 0

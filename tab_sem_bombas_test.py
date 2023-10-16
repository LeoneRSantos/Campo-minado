from tkinter import Tk

from views.tela_do_jogo import TelaDoJogo


tela = Tk()

def testar_Se_Nao_Tem_Bombas_Facil():
    t = TelaDoJogo(8,8,10,tela)
    qtdBombas = 0

    for l in range(t.linhas):
        for c in range(t.colunas):
            if t.casasRandomicas[l][c] == False:
                qtdBombas += 1

    assert qtdBombas < 64

def testar_Se_Nao_Tem_Bombas_Intermediario():
    t = TelaDoJogo(8,8,10,tela)
    qtdBombas = 0

    for l in range(t.linhas):
        for c in range(t.colunas):
            if t.casasRandomicas[l][c] == False:
                qtdBombas += 1

    assert qtdBombas < 160


def testar_Se_Nao_Tem_Bombas_Dificil():
    t = TelaDoJogo(8,8,10,tela)
    qtdBombas = 0

    for l in range(t.linhas):
        for c in range(t.colunas):
            if t.casasRandomicas[l][c] == False:
                qtdBombas += 1

    assert qtdBombas < 576




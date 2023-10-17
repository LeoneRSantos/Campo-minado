from tkinter import Tk
from views.tela_do_jogo import TelaDoJogo

tela = Tk() 
# Testar se existem espaços suficientes para as bombas

def testar_espaco_para_as_bombas_Facil():
    t = TelaDoJogo(8, 8, 10, tela)
    qtdBombas = 0
    area = t.linhas * t.colunas

    for l in range(t.linhas):
        for c in range(t.colunas):
            if t.casasRandomicas[l][c] == True:
                qtdBombas += 1

    assert area > qtdBombas


def testar_espaco_para_as_bombas_Intermediario():
    t = TelaDoJogo(10, 16, 30, tela)
    qtdBombas = 0
    area = t.linhas * t.colunas

    for l in range(t.linhas):
        for c in range(t.colunas):
            if t.casasRandomicas[l][c] == True:
                qtdBombas += 1

    assert area > qtdBombas


def testar_espaco_para_as_bombas_Dificil():
    t = TelaDoJogo(24, 24, 100, tela)
    qtdBombas = 0
    area = t.linhas * t.colunas

    for l in range(t.linhas):
        for c in range(t.colunas):
            if t.casasRandomicas[l][c] == True:
                qtdBombas += 1

    assert area > qtdBombas
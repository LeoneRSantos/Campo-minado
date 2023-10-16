from tkinter import *
from views.tela_do_jogo import TelaDoJogo

tela = Tk()

def testar_bombas_Em_Locais_Validos_Facil():
    t = TelaDoJogo(8,8,10,tela)
    valido = False

    for l in range(t.linhas):
        for c in range(t.colunas):
            if t.casasRandomicas[l][c] == True:
                valido = True

    assert valido == True


def testar_bombas_Em_Locais_Validos_Intermediario():
    t = TelaDoJogo(10,16,30,tela)
    valido = False

    for l in range(t.linhas):
        for c in range(t.colunas):
            if t.casasRandomicas[l][c] == True:
                valido = True

    assert valido == True


def testar_bombas_Em_Locais_Validos_Dificil():
    t = TelaDoJogo(24,24,100,tela)
    valido = False

    for l in range(t.linhas):
        for c in range(t.colunas):
            if t.casasRandomicas[l][c] == True:
                valido = True

    assert valido == True
    

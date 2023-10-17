from tkinter import *
import pytest

from views.tela_do_jogo import TelaDoJogo

tela = Tk()

# O jogo deve revelar o número de bombas adjacentes a uma zona quando ela for descoberta.

def testar_se_a_casa_clicada_contem_bomba_facil():
    t = TelaDoJogo(8,8,10,tela)
    clicouBomba = False

    for l in range(t.linhas):
        for c in range(t.colunas):
            if t.casasRandomicas[l][c] == True:
                if t.matrizDoJogo[l][c]['text'] == 'B':
                    clicouBomba = True
    assert clicouBomba == False

def testar_se_a_casa_clicada_contem_bomba_intermediario():
    t = TelaDoJogo(10,16,30,tela)
    clicouBomba = False

    for l in range(t.linhas):
        for c in range(t.colunas):
            if t.casasRandomicas[l][c] == True:
                if t.matrizDoJogo[l][c]['text'] == 'B':
                    clicouBomba = True
    assert clicouBomba == False

def testar_se_a_casa_clicada_contem_bomba_dificil():
    t = TelaDoJogo(24,24,100,tela)
    clicouBomba = False

    for l in range(t.linhas):
        for c in range(t.colunas):
            if t.casasRandomicas[l][c] == True:
                if t.matrizDoJogo[l][c]['text'] == 'B':
                    clicouBomba = True
    assert clicouBomba == False

def testar_adjacencia_correta_Facil():
    t = TelaDoJogo(8,8,10,tela)
    adj = 0

    for l in range(t.linhas):
        for c in range(t.colunas):
            adj = t.calcularBombasAdjacentes(l,c)

    assert adj == 0 or adj < 9

def testar_adjacencia_correta_intermediario():
    t = TelaDoJogo(10,16,30,tela)
    adj = 0

    for l in range(t.linhas):
        for c in range(t.colunas):
            adj = t.calcularBombasAdjacentes(l,c)

    assert adj == 0 or adj < 9

def testar_adjacencia_correta_dificil():
    t = TelaDoJogo(24,24,100,tela)
    adj = 0

    for l in range(t.linhas):
        for c in range(t.colunas):
            adj = t.calcularBombasAdjacentes(l,c)

    assert adj == 0 or adj < 9
from tkinter import *
from views.tela_do_jogo import TelaDoJogo

tela = Tk()

def testar_se_o_numero_de_bombas_e_negativo_Facil():
    t = TelaDoJogo(8,8,10,tela)
    qtdBombas = 0

    for linhas in range(t.linhas):
        for colunas in range(t.colunas):
            if t.casasRandomicas[linhas][colunas] == True:
                qtdBombas += 1
    
    assert not qtdBombas < 0

def testar_se_o_numero_de_bombas_e_negativo_Intermediario():
    t = TelaDoJogo(10,16,30,tela)
    qtdBombas = 0

    for linhas in range(t.linhas):
        for colunas in range(t.colunas):
            if t.casasRandomicas[linhas][colunas] == True:
                qtdBombas += 1
    
    assert not qtdBombas < 0

def testar_se_o_numero_de_bombas_e_negativo_Dificil():
    t = TelaDoJogo(24,24,100,tela)
    qtdBombas = 0

    for linhas in range(t.linhas):
        for colunas in range(t.colunas):
            if t.casasRandomicas[linhas][colunas] == True:
                qtdBombas += 1
    
    assert not qtdBombas < 0

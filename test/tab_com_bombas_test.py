from tkinter import Tk

from views.tela_do_jogo import TelaDoJogo

# Fácil

def testar_se_o_tabuleiro_so_contem_bombas_facil():
    tela = Tk()
    c = 0
    t = TelaDoJogo(8,8,10,tela)

    for l in range(t.linhas):
        for cc in range(t.colunas):
            if t.casasRandomicas[l][cc] == True:
                c += 1
    assert c < 64

# Intermediario

def testar_se_o_tabuleiro_so_contem_bombas_intermediario():
    tela = Tk()
    c = 0
    t = TelaDoJogo(10,16,30,tela)

    for l in range(t.linhas):
        for cc in range(t.colunas):
            if t.casasRandomicas[l][cc] == True:
                c += 1
    assert c < 160

# Difícil

def testar_se_o_tabuleiro_so_contem_bombas_dificil():
    tela = Tk()
    c = 0
    t = TelaDoJogo(24,24,100,tela)

    for l in range(t.linhas):
        for cc in range(t.colunas):
            if t.casasRandomicas[l][cc] == True:
                c += 1
    assert c < 576
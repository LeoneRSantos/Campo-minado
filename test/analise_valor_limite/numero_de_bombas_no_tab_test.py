from tkinter import Tk
from views.tela_do_jogo import TelaDoJogo

tela = Tk()

# Verificar se o número de bombas do tabuleiro é maior que 10 [x]
# Verificar se o número de bombas do tabuleiro é menor que 10 [x]
# Verificar se o número de bombas é exatamente 10.

def testar_se_o_numero_de_bombas_e_menor_que_dez_facil():
    t = TelaDoJogo(8,8,10,tela)
    qdtBombas = 0

    for linhas in range(t.linhas):
        for colunas in range(t.colunas):
            if t.casasRandomicas[linhas][colunas] == True:
                qdtBombas += 1

    assert not qdtBombas < 10 


def testar_se_o_numero_de_bombas_e_maior_que_dez_facil():
    t = TelaDoJogo(8,8,10,tela)
    qdtBombas = 0

    for linhas in range(t.linhas):
        for colunas in range(t.colunas):
            if t.casasRandomicas[linhas][colunas] == True:
                qdtBombas += 1

    assert not qdtBombas > 10

def testar_se_o_numero_de_bombas_e_exatamente_dez_facil():
    t = TelaDoJogo(8,8,10,tela)
    qdtBombas = 0

    for linhas in range(t.linhas):
        for colunas in range(t.colunas):
            if t.casasRandomicas[linhas][colunas] == True:
                qdtBombas += 1

    assert qdtBombas == 10


def testar_se_o_numero_de_bombas_e_menor_que_trinta_intermediario():
    t = TelaDoJogo(10,16,30,tela)
    qdtBombas = 0

    for linhas in range(t.linhas):
        for colunas in range(t.colunas):
            if t.casasRandomicas[linhas][colunas] == True:
                qdtBombas += 1

    assert not qdtBombas < 30

def testar_se_o_numero_de_bombas_e_maior_que_trinta_intermediario():
    t = TelaDoJogo(10,16,30,tela)
    qdtBombas = 0

    for linhas in range(t.linhas):
        for colunas in range(t.colunas):
            if t.casasRandomicas[linhas][colunas] == True:
                qdtBombas += 1

    assert not qdtBombas > 30

def testar_se_o_numero_de_bombas_e_exatamente_igual_a_trinta_intermediario():
    t = TelaDoJogo(10,16,30,tela)
    qdtBombas = 0

    for linhas in range(t.linhas):
        for colunas in range(t.colunas):
            if t.casasRandomicas[linhas][colunas] == True:
                qdtBombas += 1

    assert qdtBombas == 30

def testar_se_o_numero_de_bombas_e_menor_que_cem_dificil():
    t = TelaDoJogo(24,24,100,tela)
    qdtBombas = 0

    for linhas in range(t.linhas):
        for colunas in range(t.colunas):
            if t.casasRandomicas[linhas][colunas] == True:
                qdtBombas += 1

    assert not qdtBombas < 100 

def testar_se_o_numero_de_bombas_e_maior_que_cem_dificil():
    t = TelaDoJogo(24,24,100,tela)
    qdtBombas = 0

    for linhas in range(t.linhas):
        for colunas in range(t.colunas):
            if t.casasRandomicas[linhas][colunas] == True:
                qdtBombas += 1

    assert not qdtBombas > 100 

def testar_se_o_numero_de_bombas_e_exatamente_igual_a_cem_dificil():
    t = TelaDoJogo(24,24,100,tela)
    qdtBombas = 0

    for linhas in range(t.linhas):
        for colunas in range(t.colunas):
            if t.casasRandomicas[linhas][colunas] == True:
                qdtBombas += 1

    assert qdtBombas == 100 
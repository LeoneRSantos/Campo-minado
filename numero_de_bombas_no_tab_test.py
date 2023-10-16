from tkinter import Tk
from views.tela_do_jogo import TelaDoJogo

tela = Tk()

# verificar se o número de bombas do tabuleiro é maior que 10 [x]
#   verificar se o número de bombas do tabuleiro é menor que 10 [x]

def testar_se_o_numero_de_bombas_esta_correto_Facil_menor():
    t = TelaDoJogo(8,8,10,tela)
    qdtBombas = 0

    for linhas in range(t.linhas):
        for colunas in range(t.colunas):
            if t.casasRandomicas[linhas][colunas] == True:
                qdtBombas += 1

    assert not qdtBombas < 10 


def testar_se_o_numero_de_bombas_esta_correto_Facil_maior():
    t = TelaDoJogo(8,8,10,tela)
    qdtBombas = 0

    for linhas in range(t.linhas):
        for colunas in range(t.colunas):
            if t.casasRandomicas[linhas][colunas] == True:
                qdtBombas += 1

    assert not qdtBombas > 10


def testar_se_o_numero_de_bombas_esta_correto_Intermediario_menor():
    t = TelaDoJogo(10,16,30,tela)
    qdtBombas = 0

    for linhas in range(t.linhas):
        for colunas in range(t.colunas):
            if t.casasRandomicas[linhas][colunas] == True:
                qdtBombas += 1

    assert not qdtBombas < 30

def testar_se_o_numero_de_bombas_esta_correto_Intermediario_maior():
    t = TelaDoJogo(10,16,30,tela)
    qdtBombas = 0

    for linhas in range(t.linhas):
        for colunas in range(t.colunas):
            if t.casasRandomicas[linhas][colunas] == True:
                qdtBombas += 1

    assert not qdtBombas > 30

def testar_se_o_numero_de_bombas_esta_correto_Dificil_menor():
    t = TelaDoJogo(24,24,100,tela)
    qdtBombas = 0

    for linhas in range(t.linhas):
        for colunas in range(t.colunas):
            if t.casasRandomicas[linhas][colunas] == True:
                qdtBombas += 1

    assert not qdtBombas < 100 

def testar_se_o_numero_de_bombas_esta_correto_Dificil_maior():
    t = TelaDoJogo(24,24,100,tela)
    qdtBombas = 0

    for linhas in range(t.linhas):
        for colunas in range(t.colunas):
            if t.casasRandomicas[linhas][colunas] == True:
                qdtBombas += 1

    assert not qdtBombas > 100 
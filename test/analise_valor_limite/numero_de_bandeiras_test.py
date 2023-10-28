from tkinter import *

from views.tela_do_jogo import TelaDoJogo

# O software deve exibir o número de bandeiras disponíveis para uso.

tela = Tk()


def testar_numero_de_bandeiras_facil_igual_a_bombas():
    t = TelaDoJogo(8, 8, 10, tela)
    bandeiras = 0

    for l in range(t.linhas):
        for c in range(t.colunas):
            if t.casasRandomicas[l][c] == True:
                t.adicionarBandeira(t.matrizDoJogo[l][c])
                bandeiras += 1

    assert t.qtdBandeiras == bandeiras and t.bombas == bandeiras

def testar_numero_de_bandeiras_facil_maior_que_bombas():
    t = TelaDoJogo(8, 8, 10, tela)
    bandeiras = 0

    for l in range(t.linhas):
        for c in range(t.colunas):
            if t.casasRandomicas[l][c] == True:
                t.adicionarBandeira(t.matrizDoJogo[l][c])
                bandeiras += 1

    assert not t.qtdBandeiras > bandeiras and not t.bombas > bandeiras

def testar_numero_de_bandeiras_facil_menor_que_bombas():
    t = TelaDoJogo(8, 8, 10, tela)
    bandeiras = 0

    for l in range(t.linhas):
        for c in range(t.colunas):
            if t.casasRandomicas[l][c] == True:
                t.adicionarBandeira(t.matrizDoJogo[l][c])
                bandeiras += 1

    assert not t.qtdBandeiras < bandeiras and not t.bombas < bandeiras


def testar_numero_de_bandeiras_intermediario_igual_a_bombas():
    t = TelaDoJogo(10, 16, 30, tela)
    bandeiras = 0

    for l in range(t.linhas):
        for c in range(t.colunas):
            if t.casasRandomicas[l][c] == True:
                t.adicionarBandeira(t.matrizDoJogo[l][c])
                bandeiras += 1

    assert t.qtdBandeiras == bandeiras and t.bombas == bandeiras

def testar_numero_de_bandeiras_intermediario_maior_que_bombas():
    t = TelaDoJogo(10, 16, 30, tela)
    bandeiras = 0

    for l in range(t.linhas):
        for c in range(t.colunas):
            if t.casasRandomicas[l][c] == True:
                t.adicionarBandeira(t.matrizDoJogo[l][c])
                bandeiras += 1

    assert not t.qtdBandeiras > bandeiras and not t.bombas > bandeiras

def testar_numero_de_bandeiras_intermediario_menor_que_bombas():
    t = TelaDoJogo(10, 16, 30, tela)
    bandeiras = 0

    for l in range(t.linhas):
        for c in range(t.colunas):
            if t.casasRandomicas[l][c] == True:
                t.adicionarBandeira(t.matrizDoJogo[l][c])
                bandeiras += 1

    assert not t.qtdBandeiras < bandeiras and not t.bombas < bandeiras


def testar_numero_de_bandeiras_dificil_igual_a_bombas():
    t = TelaDoJogo(24, 24, 100, tela)
    bandeiras = 0

    for l in range(t.linhas):
        for c in range(t.colunas):
            if t.casasRandomicas[l][c] == True:
                t.adicionarBandeira(t.matrizDoJogo[l][c])
                bandeiras += 1

    assert t.qtdBandeiras == bandeiras and t.bombas == bandeiras

def testar_numero_de_bandeiras_dificil_maior_que_bombas():
    t = TelaDoJogo(24, 24, 100, tela)
    bandeiras = 0

    for l in range(t.linhas):
        for c in range(t.colunas):
            if t.casasRandomicas[l][c] == True:
                t.adicionarBandeira(t.matrizDoJogo[l][c])
                bandeiras += 1

    assert not t.qtdBandeiras > bandeiras and not t.bombas > bandeiras

def testar_numero_de_bandeiras_dificil_menor_que_bombas():
    t = TelaDoJogo(24, 24, 100, tela)
    bandeiras = 0

    for l in range(t.linhas):
        for c in range(t.colunas):
            if t.casasRandomicas[l][c] == True:
                t.adicionarBandeira(t.matrizDoJogo[l][c])
                bandeiras += 1

    assert not t.qtdBandeiras < bandeiras and not t.bombas < bandeiras


def testar_se_o_numero_de_bandeiras_disponivel_e_exibido():
    tf = TelaDoJogo(8, 8, 10, tela)
    ti = TelaDoJogo(10, 16, 30, tela)
    td = TelaDoJogo(24, 24, 100, tela)

    assert tf.jogoIniciado == True and ti.jogoIniciado == True and td.jogoIniciado == True

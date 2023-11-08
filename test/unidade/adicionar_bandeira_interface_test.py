from tkinter import *
from views.tela_do_jogo import TelaDoJogo
import pytest

tela = Tk()

#   - [ ] Testar se é possível adicionar uma bandeira em qualquer casa.
#   - [ ] Testar se é possível adicionar uma bandeira numa casa já verificada com adjacência.
#   - [ ] Testar se é possível adicionar uma bandeira numa casa que foi revelada contendo bomba.


@pytest.mark.parametrize("x, y, esperado", [
    (2, 3, 'P'),
    (0, 0, 'P'),
    (1, 4, 'P'),
    (2, 5, 'P')
])
def testar_se_e_possivel_adicionar_bandeira_em_qualquer_casa_facil(x, y, esperado):
    tf = TelaDoJogo(8, 8, 10, tela)

    tf.adicionarBandeira(x, y)

    assert tf.matrizDoJogo[x][y]['text'] == esperado


@pytest.mark.parametrize("x, y, esperado", [
    (2, 3, 'P'),
    (0, 0, 'P'),
    (1, 4, 'P'),
    (2, 5, 'P')
])
def testar_se_e_possivel_adicionar_bandeira_em_qualquer_casa_intermediario(x, y, esperado):
    ti = TelaDoJogo(10, 16, 30, tela)

    ti.adicionarBandeira(x, y)

    assert ti.matrizDoJogo[x][y]['text'] == esperado


@pytest.mark.parametrize("x, y, esperado", [
    (2, 3, 'P'),
    (0, 0, 'P'),
    (1, 4, 'P'),
    (2, 5, 'P')
])
def testar_se_e_possivel_adicionar_bandeira_em_qualquer_casa_dificil(x, y, esperado):
    td = TelaDoJogo(24, 24, 100, tela)

    td.adicionarBandeira(x, y)

    assert td.matrizDoJogo[x][y]['text'] == esperado


def testar_adicionar_bandeira_em_casa_com_adjacencia_facil():
    tf = TelaDoJogo(8, 8, 10, tela)

    tf.casasRandomicas[2][4] = False

    try:
        tf.verificarCasa(tf.matrizDoJogo[2][4])
    except:
        RecursionError

    tf.adicionarBandeira(2, 4)

    assert tf.matrizDoJogo[2][4]['text'] == str(
        tf.calcularBombasAdjacentes(2, 4))


def testar_adicionar_bandeira_em_casa_com_adjacencia_intermediario():
    ti = TelaDoJogo(10, 16, 30, tela)

    ti.casasRandomicas[2][4] = False

    try:

        ti.verificarCasa(ti.matrizDoJogo[2][4])
    except:
        RecursionError

    ti.adicionarBandeira(2, 4)

    assert ti.matrizDoJogo[2][4]['text'] == str(
        ti.calcularBombasAdjacentes(2, 4))


def testar_adicionar_bandeira_em_casa_com_adjacencia_dificil():
    td = TelaDoJogo(24, 24, 30, tela)

    td.casasRandomicas[2][4] = False

    try:
        td.verificarCasa(td.matrizDoJogo[2][4])
    except:
        RecursionError

    td.adicionarBandeira(2, 4)

    assert td.matrizDoJogo[2][4]['text'] == str(
        td.calcularBombasAdjacentes(2, 4))


def testar_adicionar_bandeira_em_casa_verificada_com_bomba_facil():
    tf = TelaDoJogo(8, 8, 10, tela)

    tf.casasRandomicas[1][4] = True

    tf.verificarCasa(tf.matrizDoJogo[1][4])

    assert tf.matrizDoJogo[1][4]['text'] == 'X'

def testar_adicionar_bandeira_em_casa_verificada_com_bomba_intermediario():
    ti = TelaDoJogo(10, 16, 30, tela)

    ti.casasRandomicas[1][4] = True

    ti.verificarCasa(ti.matrizDoJogo[1][4])

    assert ti.matrizDoJogo[1][4]['text'] == 'X'

def testar_adicionar_bandeira_em_casa_verificada_com_bomba_dificil():
    td = TelaDoJogo(24, 24, 100, tela)

    td.casasRandomicas[1][4] = True

    td.verificarCasa(td.matrizDoJogo[1][4])

    assert td.matrizDoJogo[1][4]['text'] == 'X'

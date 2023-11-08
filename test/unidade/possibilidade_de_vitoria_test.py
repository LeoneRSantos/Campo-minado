from tkinter import *
from unittest.mock import Mock
from views.tela_do_jogo import TelaDoJogo

tela = Tk()

#   - [ ] Testar se é possível vencer.
#   - [ ] Testar se a tela de vitória é gerada.

def testar_se_e_possivel_vencer_facil():
    tf = TelaDoJogo(8, 8, 10, tela)

    for i in range(tf.linhas):
        for j in range(tf.colunas):
            if tf.casasRandomicas[i][j] == True:
                tf.adicionarBandeira(i, j)
    try:
        tf.verificarVitoria()
    except:
        AttributeError

    assert tf.venceu == True


def testar_se_e_possivel_vencer_intermediario():
    ti = TelaDoJogo(10, 16, 30, tela)

    for i in range(ti.linhas):
        for j in range(ti.colunas):
            if ti.casasRandomicas[i][j] == True:
                ti.adicionarBandeira(i, j)
    try:
        ti.verificarVitoria()
    except:
        AttributeError

    assert ti.venceu == True


def testar_se_e_possivel_vencer_dificil():
    td = TelaDoJogo(24, 24, 100, tela)

    for i in range(td.linhas):
        for j in range(td.colunas):
            if td.casasRandomicas[i][j] == True:
                td.adicionarBandeira(i, j)
    try:
        td.verificarVitoria()
    except:
        AttributeError

    assert td.venceu == True

def testar_se_a_tela_de_vitoria_e_gerada_facil():
    tf = TelaDoJogo(8, 8, 10, tela)

    facil = Mock(spec=Label(Toplevel(tf.root), text="Parabéns! Você conseguiu vencer o jogo.").pack())

    facil.assert_called

def testar_se_a_tela_de_vitoria_e_gerada_intermediario():
    ti = TelaDoJogo(10, 16, 30, tela)

    itermediario = Mock(spec=Label(Toplevel(ti.root), text="Parabéns! Você conseguiu vencer o jogo.").pack())

    itermediario.assert_called

def testar_se_a_tela_de_vitoria_e_gerada_dificil():
    td = TelaDoJogo(24, 24, 100, tela)

    dificil = Mock(spec=Label(Toplevel(td.root), text="Parabéns! Você conseguiu vencer o jogo.").pack())

    dificil.assert_called

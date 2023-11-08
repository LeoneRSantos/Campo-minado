from tkinter import *
from views.tela_do_jogo import TelaDoJogo
from views.tela_inicial import TelaInicial
from unittest.mock import Mock

tela = Tk()
telaInicial = TelaInicial(tela)


def testar_geracao_da_tela_facil():
    tf = TelaDoJogo(8, 8, 10, tela)
    geracao = Mock(side_effect=tf.jogar)

    geracao.assert_called_once_with

def testar_geracao_da_tela_intermediario():
    ti = TelaDoJogo(10, 16, 30, tela)
    geracao = Mock(side_effect=ti.jogar)

    geracao.assert_called_once_with

def testar_geracao_da_tela_dificil():
    td = TelaDoJogo(24, 24, 100, tela)
    geracao = Mock(side_effect=td.jogar)

    geracao.assert_called_once_with

def testar_geracao_da_tela_de_tutorial_facil():
    tf = TelaDoJogo(8, 8, 10, tela)
    geracao = Mock(side_effect=tf.jogar)

    geracao.assert_called_once_with
    assert tf.jogoIniciado == True

def testar_geracao_da_tela_de_tutorial_intermediario():
    ti = TelaDoJogo(10, 16, 30, tela)
    geracao = Mock(side_effect=ti.jogar)

    geracao.assert_called_once_with
    assert ti.jogoIniciado == True

def testar_geracao_da_tela_de_tutorial_dificil():
    td = TelaDoJogo(24, 24, 100, tela)
    geracao = Mock(side_effect=td.jogar)

    geracao.assert_called_once_with
    assert td.jogoIniciado == True


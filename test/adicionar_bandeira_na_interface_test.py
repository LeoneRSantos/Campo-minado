from tkinter import *
from views.tela_do_jogo import TelaDoJogo

tela = Tk()


def testar_adicionar_bandeira_na_interface_facil():
    tf = TelaDoJogo(8, 8, 10, tela)

    tf.adicionarBandeira(2, 3)

    assert tf.matrizDoJogo[2][3]['text'] == 'P'


def testar_adicionar_bandeira_na_interface_intermediario():
    ti = TelaDoJogo(10, 16, 30, tela)

    ti.adicionarBandeira(2, 3)

    assert ti.matrizDoJogo[2][3]['text'] == 'P'


def testar_adicionar_bandeira_na_interface_dificil():
    td = TelaDoJogo(24, 24, 100, tela)

    td.adicionarBandeira(2, 3)

    assert td.matrizDoJogo[2][3]['text'] == 'P'


def testar_se_e_possivel_remover_uma_bandeira_na_interface_facil():
    tf = TelaDoJogo(8, 8, 10, tela)

    tf.adicionarBandeira(3,4)
    tf.adicionarBandeira(0,5)
    tf.adicionarBandeira(3,4)

    assert tf.matrizDoJogo[3][4]['text'] == ''

def testar_se_e_possivel_remover_uma_bandeira_na_interface_intermediario():
    ti = TelaDoJogo(8, 8, 10, tela)

    ti.adicionarBandeira(3,4)
    ti.adicionarBandeira(0,5)
    ti.adicionarBandeira(3,4)

    assert ti.matrizDoJogo[3][4]['text'] == ''

def testar_se_e_possivel_remover_uma_bandeira_na_interface_dificil():
    td = TelaDoJogo(8, 8, 10, tela)

    td.adicionarBandeira(3,4)
    td.adicionarBandeira(0,5)
    td.adicionarBandeira(3,4)

    assert td.matrizDoJogo[3][4]['text'] == ''

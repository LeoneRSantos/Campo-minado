from tkinter import *

from views.tela_do_jogo import TelaDoJogo

tela = Tk()


def testar_se_o_jogo_continua_apos_adicionar_bandeira_facil():
    tf = TelaDoJogo(8, 8, 10, tela)

    tf.adicionarBandeira(2, 2)
    tf.adicionarBandeira(2, 2)

    assert tf.perdeu == False


def testar_se_o_jogo_continua_apos_adicionar_bandeira_intermediario():
    ti = TelaDoJogo(10, 16, 30, tela)

    ti.adicionarBandeira(4, 2)
    ti.adicionarBandeira(0, 0)

    assert ti.perdeu == False


def testar_se_o_jogo_continua_apos_adicionar_bandeira_dificil():
    td = TelaDoJogo(24, 24, 100, tela)

    td.adicionarBandeira(3, 4)
    td.adicionarBandeira(5, 2)

    assert td.perdeu == False


def testar_se_o_jogo_para_apos_adicionar_bandeira_facil():
    tf = TelaDoJogo(8, 8, 10, tela)
    para = False

    tf.adicionarBandeira(2, 2)

    if tf.matrizDoJogo[2][2]['text'] == 'P':
        if tf.perdeu == True:
            para = True

    assert para == False


def testar_se_o_jogo_para_apos_adicionar_bandeira_intermediario():
    ti = TelaDoJogo(10, 16, 30, tela)
    para = False

    ti.adicionarBandeira(7, 8)

    if ti.matrizDoJogo[7][8]['text'] == 'P':
        if ti.perdeu == True:
            para = True

    assert para == False


def testar_se_o_jogo_para_apos_adicionar_bandeira_dificil():
    tf = TelaDoJogo(24, 24, 100, tela)
    para = False

    tf.adicionarBandeira(20, 18)

    if tf.matrizDoJogo[20][18]['text'] == 'P':
        if tf.perdeu == True:
            para = True

    assert para == False

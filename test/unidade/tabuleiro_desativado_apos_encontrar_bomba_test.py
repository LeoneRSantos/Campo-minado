from tkinter import *
from views.tela_do_jogo import TelaDoJogo

tela = Tk()


def testar_tabuleiro_desativado_ao_encontrar_bomba_facil():
    tf = TelaDoJogo(8, 8, 10, tela)
    tf.casasRandomicas[4][5] = True

    tf.verificarCasa(tf.matrizDoJogo[4][5])

    assert tf.matrizDoJogo[0][0]['state'] == 'disabled'


def testar_tabuleiro_desativado_ao_encontrar_bomba_intermediario():
    ti = TelaDoJogo(10, 16, 30, tela)
    ti.casasRandomicas[4][5] = True

    ti.verificarCasa(ti.matrizDoJogo[4][5])

    assert ti.matrizDoJogo[1][2]['state'] == 'disabled'


def testar_tabuleiro_desativado_ao_encontrar_bomba_dificil():
    td = TelaDoJogo(24, 24, 100, tela)
    td.casasRandomicas[4][5] = True

    td.verificarCasa(td.matrizDoJogo[4][5])

    assert td.matrizDoJogo[8][8]['state'] == 'disabled'


def testar_se_as_demais_casas_permanecem_como_estao_facil():
    tf = TelaDoJogo(8, 8, 10, tela)

    tf.casasRandomicas[2][2] = False
    tf.casasRandomicas[3][3] = True

    tf.verificarCasa(tf.matrizDoJogo[2][2])
    tf.verificarCasa(tf.matrizDoJogo[3][3])

    assert tf.matrizDoJogo[2][2]['text'] == str(
        tf.calcularBombasAdjacentes(2, 2))


def testar_se_as_demais_casas_permanecem_como_estao_intermediario():
    ti = TelaDoJogo(10, 16, 30, tela)

    ti.casasRandomicas[2][2] = False
    ti.casasRandomicas[3][3] = True

    ti.verificarCasa(ti.matrizDoJogo[2][2])
    ti.verificarCasa(ti.matrizDoJogo[3][3])

    assert ti.matrizDoJogo[2][2]['text'] == str(
        ti.calcularBombasAdjacentes(2, 2))


def testar_se_as_demais_casas_permanecem_como_estao_dificil():
    td = TelaDoJogo(24, 24, 100, tela)

    td.casasRandomicas[2][2] = False
    td.casasRandomicas[3][3] = True

    td.verificarCasa(td.matrizDoJogo[2][2])
    td.verificarCasa(td.matrizDoJogo[3][3])

    assert td.matrizDoJogo[2][2]['text'] == str(
        td.calcularBombasAdjacentes(2, 2))

def testar_se_novas_casas_sao_reveladas_facil():
    tf = TelaDoJogo(8,8,10,tela)

    tf.casasRandomicas[5][2] = True
    tf.casasRandomicas[0][3] = False

    tf.verificarCasa(tf.matrizDoJogo[5][2])

    assert tf.matrizDoJogo[0][3]['text'] == ''

def testar_se_novas_casas_sao_reveladas_intermediario():
    ti = TelaDoJogo(10,16,30,tela)

    ti.casasRandomicas[5][2] = True
    ti.casasRandomicas[0][3] = False

    ti.verificarCasa(ti.matrizDoJogo[5][2])

    assert ti.matrizDoJogo[0][3]['text'] == ''

def testar_se_novas_casas_sao_reveladas_dificil():
    tf = TelaDoJogo(24,24,100,tela)

    tf.casasRandomicas[5][2] = True

    tf.verificarCasa(tf.matrizDoJogo[5][2])

    assert tf.matrizDoJogo[0][3]['text'] == ''

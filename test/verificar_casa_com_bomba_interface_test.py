from tkinter import *
from views.tela_do_jogo import TelaDoJogo

tela = Tk()


def testar_se_as_bombas_sao_mostradas_apos_encontrar_bomba_facil():
    tf = TelaDoJogo(8, 8, 10, tela)
    tf.revelarBombas()

    for l in range(tf.linhas):
        for c in range(tf.colunas):
            if tf.casasRandomicas[l][c] == True:
                assert tf.matrizDoJogo[l][c]['text'] == 'X'


def testar_se_as_bombas_sao_mostradas_apos_encontrar_bomba_intermediario():
    ti = TelaDoJogo(10, 16, 30, tela)
    ti.revelarBombas()

    for l in range(ti.linhas):
        for c in range(ti.colunas):
            if ti.casasRandomicas[l][c] == True:
                assert ti.matrizDoJogo[l][c]['text'] == 'X'


def testar_se_as_bombas_sao_mostradas_apos_encontrar_bomba_dificil():
    ti = TelaDoJogo(24, 24, 100, tela)

    ti.revelarBombas()

    for l in range(ti.linhas):
        for c in range(ti.colunas):
            if ti.casasRandomicas[l][c] == True:
                assert ti.matrizDoJogo[l][c]['text'] == 'X'


def testar_se_e_possivel_verificar_casa_com_bomba_facil():
    tf = TelaDoJogo(8, 8, 10, tela)
    possivelVerificar = False

    for l in range(tf.linhas):
        for c in range(tf.colunas):
            if tf.casasRandomicas[l][c] == True:
                try:
                    tf.verificarCasa(tf.matrizDoJogo[l][c])
                except RecursionError:
                    possivelVerificar = False

                if tf.matrizDoJogo[l][c]['text'] == 'X':
                    possivelVerificar = True

    assert possivelVerificar == True


def testar_se_e_possivel_verificar_casa_com_bomba_intermediario():
    ti = TelaDoJogo(10, 16, 30, tela)
    possivelVerificar = False

    for l in range(ti.linhas):
        for c in range(ti.colunas):
            if ti.casasRandomicas[l][c] == True:
                try:
                    ti.verificarCasa(ti.matrizDoJogo[l][c])
                except RecursionError:
                    possivelVerificar = False

                if ti.matrizDoJogo[l][c]['text'] == 'X':
                    possivelVerificar = True

    assert possivelVerificar == True


def testar_se_e_possivel_verificar_casa_com_bomba_dificil():
    td = TelaDoJogo(24, 24, 30, tela)
    possivelVerificar = False

    for l in range(td.linhas):
        for c in range(td.colunas):
            if td.casasRandomicas[l][c] == True:
                try:
                    td.verificarCasa(td.matrizDoJogo[l][c])
                except:
                    RecursionError

                if td.matrizDoJogo[l][c]['text'] == 'X':
                    possivelVerificar = True

    assert possivelVerificar == True


def testar_se_as_bombas_sao_mostradas_com_destaque_facil():
    tf = TelaDoJogo(8, 8, 10, tela)

    cor1 = ''
    cor2 = ''

    for l in range(tf.linhas):
        for c in range(tf.colunas):
            if tf.casasRandomicas[l][c] == True:
                try:
                    tf.verificarCasa(tf.matrizDoJogo[l][c])
                except:
                    RecursionError
                cor1 = tf.matrizDoJogo[l][c]['bg']

            else:
                cor2 = tf.matrizDoJogo[l][c]['bg']

    assert cor1 != cor2


def testar_se_as_bombas_sao_mostradas_com_destaque_intermediario():
    ti = TelaDoJogo(10, 16, 30, tela)

    cor1 = ''
    cor2 = ''

    for l in range(ti.linhas):
        for c in range(ti.colunas):
            if ti.casasRandomicas[l][c] == True:
                try:
                    ti.verificarCasa(ti.matrizDoJogo[l][c])
                except:
                    RecursionError
                cor1 = ti.matrizDoJogo[l][c]['bg']
            else:
                cor2 = ti.matrizDoJogo[l][c]['bg']

    assert cor1 != cor2

def testar_se_as_bombas_sao_mostradas_com_destaque_dificil():
    td = TelaDoJogo(24, 24, 100, tela)

    cor1 = ''
    cor2 = ''

    for l in range(td.linhas):
        for c in range(td.colunas):
            if td.casasRandomicas[l][c] == True:
                try:
                    td.verificarCasa(td.matrizDoJogo[l][c])
                except:
                    RecursionError
                cor1 = td.matrizDoJogo[l][c]['bg']
            else:
                cor2 = td.matrizDoJogo[l][c]['bg']

    assert cor1 != cor2


def testar_se_as_demais_casas_sem_bomba_sao_afetadas_ao_encontrar_bomba_facil():
    tf = TelaDoJogo(8, 8, 10, tela)
    alteradas = False

    tf.revelarBombas()

    for l in range(tf.linhas):
        for c in range(tf.colunas):
            if tf.casasRandomicas[l][c] == False:
                if tf.matrizDoJogo[l][c]['text'] != '':
                    alteradas = True

    assert alteradas == False

def testar_se_as_demais_casas_sem_bomba_sao_afetadas_ao_encontrar_bomba_intermediario():
    ti = TelaDoJogo(10, 16, 30, tela)
    alteradas = False

    ti.revelarBombas()

    for l in range(ti.linhas):
        for c in range(ti.colunas):
            if ti.casasRandomicas[l][c] == False:
                if ti.matrizDoJogo[l][c]['text'] != '':
                    alteradas = True

    assert alteradas == False

def testar_se_as_demais_casas_sem_bomba_sao_afetadas_ao_encontrar_bomba_dificil():
    td = TelaDoJogo(24, 24, 100, tela)
    alteradas = False

    td.revelarBombas()

    for l in range(td.linhas):
        for c in range(td.colunas):
            if td.casasRandomicas[l][c] == False:
                if td.matrizDoJogo[l][c]['text'] != '':
                    alteradas = True

    assert alteradas == False

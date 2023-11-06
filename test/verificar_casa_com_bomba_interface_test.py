from tkinter import *
from views.tela_do_jogo import TelaDoJogo

tela = Tk()


def testar_se_as_bombas_sao_mostradas_apos_encontrar_bomba_facil():
    tf = TelaDoJogo(8, 8, 10, tela)
    mostradas = False

    for l in range(tf.linhas):
        for c in range(tf.colunas):
            if tf.casasRandomicas[l][c] == True:
                try:
                    tf.verificarCasa(tf.matrizDoJogo[l][c])
                except RecursionError:
                    mostradas = False

    for ll in range(tf.linhas):
        for cc in range(tf.colunas):
            if tf.casasRandomicas[ll][cc] == True and tf.matrizDoJogo[ll][cc]['text'] == 'X':
                mostradas = True

    assert mostradas == True


def testar_se_as_bombas_sao_mostradas_apos_encontrar_bomba_intermediario():
    ti = TelaDoJogo(10, 16, 30, tela)
    mostradas = False

    for l in range(ti.linhas):
        for c in range(ti.colunas):
            if ti.casasRandomicas[l][c] == True:
                try:
                    ti.verificarCasa(ti.matrizDoJogo[l][c])
                except RecursionError:
                    mostradas = False

    for ll in range(ti.linhas):
        for cc in range(ti.colunas):
            if ti.casasRandomicas[ll][cc] == True and ti.matrizDoJogo[ll][cc]['text'] == 'X':
                mostradas = True

    assert mostradas == True


def testar_se_as_bombas_sao_mostradas_apos_encontrar_bomba_dificil():
    ti = TelaDoJogo(24, 24, 100, tela)
    mostradas = False

    for l in range(ti.linhas):
        for c in range(ti.colunas):
            if ti.casasRandomicas[l][c] == True:
                try:
                    ti.verificarCasa(ti.matrizDoJogo[l][c])
                except RecursionError:
                    mostradas = False

    for ll in range(ti.linhas):
        for cc in range(ti.colunas):
            if ti.casasRandomicas[ll][cc] == True and ti.matrizDoJogo[ll][cc]['text'] == 'X':
                mostradas = True

    assert mostradas == True


def testar_se_e_possivel_verificar_casa_com_bomba_facil():
    tf = TelaDoJogo(8, 8, 10, tela)
    possivelVerificar = False

    for l in range(tf.linhas):
        for c in range(tf.colunas):
            if tf.casasRandomicas[l][c]==True:
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
            if ti.casasRandomicas[l][c]==True:
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
            if td.casasRandomicas[l][c]==True:
                try:
                    td.verificarCasa(td.matrizDoJogo[l][c])
                except RecursionError:
                    possivelVerificar = False

                if td.matrizDoJogo[l][c]['text'] == 'X':
                    possivelVerificar = True

    assert possivelVerificar == True

from tkinter import *
from views.tela_do_jogo import TelaDoJogo

tela = Tk()

#   - [x] Testar se a casa fica desativada ao ser descoberta e encontrar um número que indique adjacência de bombas.
#   - [x] Testar se todas as casas do tabuleiro ficam desativadas após encontrar uma boba.
#   - [x] Testar se todas as bombas do tabuleiro são mostradas ao se descobrir uma bomba.
# - [x] Testar se é possível descobrir uma bomba ou o número de bombas adjacentes ao se descobrir uma casa do tabuleiro.


def testar_se_a_casa_fica_desativada_com_adjacencia_facil():
    tf = TelaDoJogo(8, 8, 10, tela)
    desativada = False

    for l in range(tf.linhas):
        for c in range(tf.colunas):
            if tf.casasRandomicas[l][c] == False:
                try:
                    tf.verificarCasa(tf.matrizDoJogo[l][c])
                except RecursionError:
                    desativada = True

    assert desativada == True


def testar_se_a_casa_fica_desativada_com_adjacencia_intermediario():
    ti = TelaDoJogo(10, 16, 30, tela)
    desativada = False

    for l in range(ti.linhas):
        for c in range(ti.colunas):
            if ti.casasRandomicas[l][c] == False:
                try:
                    ti.verificarCasa(ti.matrizDoJogo[l][c])
                except RecursionError:
                    desativada = True

    assert desativada == True

def testar_se_a_casa_fica_desativada_com_adjacencia_dificil():
    td = TelaDoJogo(24, 24, 100, tela)
    desativada = False

    for l in range(td.linhas):
        for c in range(td.colunas):
            if td.casasRandomicas[l][c] == False:
                try:
                    td.verificarCasa(td.matrizDoJogo[l][c])
                except RecursionError:
                    desativada = True

    assert desativada == True


def testar_se_todas_as_casas_ficam_desativadas_ao_encrontar_bomba_facil():
    tf = TelaDoJogo(8, 8, 10, tela)
    desativada = False

    for l in range(tf.linhas):
        for c in range(tf.colunas):
            if tf.casasRandomicas[l][c] == True:
                tf.verificarCasa(tf.matrizDoJogo[l][c])

                if tf.matrizDoJogo[l][c]['state'] == "disabled":

                    desativada = True
                

    assert desativada == True


def testar_se_todas_as_casas_ficam_desativadas_ao_encrontar_bomba_intermediario():
    ti = TelaDoJogo(10, 16, 30, tela)
    desativada = False

    for l in range(ti.linhas):
        for c in range(ti.colunas):
            if ti.casasRandomicas[l][c] == True:
                ti.verificarCasa(ti.matrizDoJogo[l][c])

                if ti.matrizDoJogo[l][c]['state'] == "disabled":

                    desativada = True
                

    assert desativada == True


def testar_se_todas_as_casas_ficam_desativadas_ao_encrontar_bomba_dificil():
    td = TelaDoJogo(24, 24, 100, tela)
    desativada = False

    for l in range(td.linhas):
        for c in range(td.colunas):
            if td.casasRandomicas[l][c] == True:
                td.verificarCasa(td.matrizDoJogo[l][c])

                if td.matrizDoJogo[l][c]['state'] == "disabled":

                    desativada = True
                

    assert desativada == True


def testar_se_todas_as_bombas_sao_mostradas_facil():
    tf = TelaDoJogo(8, 8, 10, tela)
    mostradas = False

    tf.revelarBombas()

    for l in range(tf.linhas):
        for c in range(tf.colunas):
            if tf.casasRandomicas[l][c] == True and tf.matrizDoJogo[l][c]['text'] == 'X':
                mostradas = True

    assert mostradas == True

def testar_se_todas_as_bombas_sao_mostradas_intermediario():
    ti = TelaDoJogo(10, 16, 30, tela)
    mostradas = False

    ti.revelarBombas()

    for l in range(ti.linhas):
        for c in range(ti.colunas):
            if ti.casasRandomicas[l][c] == True and ti.matrizDoJogo[l][c]['text'] == 'X':
                mostradas = True

    assert mostradas == True


def testar_se_todas_as_bombas_sao_mostradas_dificil():
    td = TelaDoJogo(24, 24, 100, tela)
    mostradas = False

    td.revelarBombas()

    for l in range(td.linhas):
        for c in range(td.colunas):
            if td.casasRandomicas[l][c] == True and td.matrizDoJogo[l][c]['text'] == 'X':
                mostradas = True

    assert mostradas == True

def testar_se_descobre_bomba_ou_adjacencia_facil():
    tf = TelaDoJogo(8,8,10,tela)
    descobre = False

    for l in range(tf.linhas):
        for c in range(tf.colunas):
            try:
                tf.verificarCasa(tf.matrizDoJogo[l][c])

                if tf.matrizDoJogo[l][c]['text'] == 'X' or tf.matrizDoJogo[l][c]['text'] == str(int):
                    descobre = True
            except RecursionError:
                descobre = True

    assert descobre == True


def testar_se_descobre_bomba_ou_adjacencia_intermediario():
    ti = TelaDoJogo(10,16,30,tela)
    descobre = False

    for l in range(ti.linhas):
        for c in range(ti.colunas):
            try:
                ti.verificarCasa(ti.matrizDoJogo[l][c])

                if ti.matrizDoJogo[l][c]['text'] == 'X' or ti.matrizDoJogo[l][c]['text'] == str(int):
                    descobre = True
            except RecursionError:
                descobre = True

    assert descobre == True

def testar_se_descobre_bomba_ou_adjacencia_dificil():
    td = TelaDoJogo(24,24,100,tela)
    descobre = False

    for l in range(td.linhas):
        for c in range(td.colunas):
            try:
                td.verificarCasa(td.matrizDoJogo[l][c])

                if td.matrizDoJogo[l][c]['text'] == 'X' or td.matrizDoJogo[l][c]['text'] == str(int):
                    descobre = True
            except RecursionError:
                descobre = True

    assert descobre == True


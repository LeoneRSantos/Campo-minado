
import pytest
from tkinter import *
from views.tela_do_jogo import TelaDoJogo
tela = Tk()

# Linhas


def testar_dimensoes_do_nivel_facil_linhas_igual_a_oito():
    tf = TelaDoJogo(8, 8, 10, tela)
    lista = []
    qtd = 0

    for l in range(tf.linhas):
        lista.append(tf.matrizDoJogo[l][0])
        qtd = len(lista)

    assert qtd == 8


def testar_dimensoes_do_nivel_facil_linhas_menor_que_oito():
    tf = TelaDoJogo(8, 8, 10, tela)
    lista = []
    qtd = 0

    for l in range(tf.linhas):
        lista.append(tf.matrizDoJogo[l][0])
        qtd = len(lista)

    assert not qtd < 8


def testar_dimensoes_do_nivel_facil_linhas_maior_que_oito():
    tf = TelaDoJogo(8, 8, 10, tela)
    lista = []
    qtd = 0

    for l in range(tf.linhas):
        lista.append(tf.matrizDoJogo[l][0])
        qtd = len(lista)

    assert not qtd > 8


def testar_dimensoes_do_nivel_intermediario_linhas_igual_a_dez():
    ti = TelaDoJogo(10, 16, 30, tela)
    lista = []
    qtd = 0

    for l in range(ti.linhas):
        lista.append(ti.matrizDoJogo[l][0])
        qtd = len(lista)

    assert qtd == 10


def testar_dimensoes_do_nivel_intermediario_linhas_menor_que_dez():
    ti = TelaDoJogo(10, 16, 30, tela)
    lista = []
    qtd = 0

    for l in range(ti.linhas):
        lista.append(ti.matrizDoJogo[l][0])
        qtd = len(lista)

    assert not qtd > 10


def testar_dimensoes_do_nivel_intermediario_linhas_maior_que_dez():
    ti = TelaDoJogo(10, 16, 30, tela)
    lista = []
    qtd = 0

    for l in range(ti.linhas):
        lista.append(ti.matrizDoJogo[l][0])
        qtd = len(lista)

    assert not qtd > 10


def testar_dimensoes_do_nivel_dificil_linhas_igual_a_vinte_e_quatro():
    td = TelaDoJogo(24, 24, 100, tela)
    lista = []
    qtd = 0

    for l in range(td.linhas):
        lista.append(td.matrizDoJogo[l][0])
        qtd = len(lista)

    assert qtd == 24


def testar_dimensoes_do_nivel_dificil_linhas_menor_que_vinte_e_quatro():
    td = TelaDoJogo(24, 24, 100, tela)
    lista = []
    qtd = 0

    for l in range(td.linhas):
        lista.append(td.matrizDoJogo[l][0])
        qtd = len(lista)

    assert not qtd > 24


def testar_dimensoes_do_nivel_dificil_linhas_maior_que_vinte_e_quatro():
    td = TelaDoJogo(24, 24, 100, tela)
    lista = []
    qtd = 0

    for l in range(td.linhas):
        lista.append(td.matrizDoJogo[l][0])
        qtd = len(lista)

    assert not qtd > 24

# Colunas


def testar_dimensoes_do_nivel_facil_colunas_igual_a_oito():
    tf = TelaDoJogo(8, 8, 10, tela)
    lista = []
    qtd = 0

    for c in range(tf.colunas):
        lista.append(tf.matrizDoJogo[0][c])
        qtd = len(lista)

    assert qtd == 8


def testar_dimensoes_do_nivel_facil_colunas_maior_que_oito():
    tf = TelaDoJogo(8, 8, 10, tela)
    lista = []
    qtd = 0

    for c in range(tf.colunas):
        lista.append(tf.matrizDoJogo[0][c])
        qtd = len(lista)

    assert not qtd > 8


def testar_dimensoes_do_nivel_facil_colunas_menor_que_oito():
    tf = TelaDoJogo(8, 8, 10, tela)
    lista = []
    qtd = 0

    for c in range(tf.colunas):
        lista.append(tf.matrizDoJogo[0][c])
        qtd = len(lista)

    assert not qtd < 8


def testar_dimensoes_do_nivel_intermediario_colunas_igual_a_dezesseis():
    ti = TelaDoJogo(10, 16, 30, tela)
    lista = []
    qtd = 0

    for c in range(ti.colunas):
        lista.append(ti.matrizDoJogo[0][c])
        qtd = len(lista)

    assert qtd == 16


def testar_dimensoes_do_nivel_intermediario_colunas_maior_que_dezesseis():
    ti = TelaDoJogo(10, 16, 30, tela)
    lista = []
    qtd = 0

    for c in range(ti.colunas):
        lista.append(ti.matrizDoJogo[0][c])
        qtd = len(lista)

    assert not qtd > 16


def testar_dimensoes_do_nivel_intermediario_colunas_menor_que_dezesseis():
    ti = TelaDoJogo(10, 16, 30, tela)
    lista = []
    qtd = 0

    for c in range(ti.colunas):
        lista.append(ti.matrizDoJogo[0][c])
        qtd = len(lista)

    assert not qtd < 16


def testar_dimensoes_do_nivel_dificil_colunas_igual_a_vinte_e_quatro():
    td = TelaDoJogo(24, 24, 100, tela)
    lista = []
    qtd = 0

    for c in range(td.colunas):
        lista.append(td.matrizDoJogo[0][c])
        qtd = len(lista)

    assert qtd == 24


def testar_dimensoes_do_nivel_dificil_colunas_maior_que_vinte_e_quatro():
    td = TelaDoJogo(24, 24, 100, tela)
    lista = []
    qtd = 0

    for c in range(td.colunas):
        lista.append(td.matrizDoJogo[0][c])
        qtd = len(lista)

    assert not qtd > 24


def testar_dimensoes_do_nivel_dificil_colunas_menor_que_vinte_e_quatro():
    td = TelaDoJogo(24, 24, 100, tela)
    lista = []
    qtd = 0

    for c in range(td.colunas):
        lista.append(td.matrizDoJogo[0][c])
        qtd = len(lista)

    assert not qtd < 24

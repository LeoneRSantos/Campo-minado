from tkinter import Tk
import pytest
from jogo.dificuldade import Dificuldade
from views.tela_do_jogo import TelaDoJogo
from views.tela_inicial import TelaInicial

tela = Tk()

# Testar marcações inválidas.


@pytest.mark.parametrize("linha, coluna", [
    (0, 13), (4, 10), (-2, 9), (2, 20),
    (1, 18), (4, 24), (6, 11), (0, 23),
    (30, 3), (-4, 18), (3, 11), (0, 10),
])
def testar_marcacao_invalida_facil(linha, coluna):
    valido = True
    tf = TelaDoJogo(8, 8, 10, tela)

    for l in range(11):
        for c in range(11):
            try:
                tf.verificarCasa(tf.matrizDoJogo[linha][coluna])
            except IndexError:
                valido = False

    assert valido == False


@pytest.mark.parametrize("linha, coluna", [
    (0, 20), (4, 17), (4, 17), (2, 22),
    (1, 18), (4, 24), (6, 21), (0, 23),
    (30, 3), (-4, 18), (12, 11), (0, 17),
])
def testar_marcacao_invalida_intermediario(linha, coluna):
    valido = True
    ti = TelaDoJogo(10, 16, 30, tela)

    for l in range(11):
        for c in range(11):
            try:
                ti.verificarCasa(ti.matrizDoJogo[linha][coluna])
            except IndexError:
                valido = False

    assert valido == False


@pytest.mark.parametrize("linha, coluna", [
    (2, 25), (14, 27), (28, 17), (26, 22),
    (1, 26), (80, 24), (62, 21), (0, 30),
    (30, 3), (-4, 26), (12, 50), (0, 34),
])
def testar_marcacao_invalida_dificil(linha, coluna):
    valido = True
    td = TelaDoJogo(24, 24, 100, tela)

    for l in range(11):
        for c in range(11):
            try:
                td.verificarCasa(td.matrizDoJogo[linha][coluna])
            except IndexError:
                valido = False

    assert valido == False

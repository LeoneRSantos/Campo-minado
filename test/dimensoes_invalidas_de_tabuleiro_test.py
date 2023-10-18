from tkinter import Tk
import pytest
from jogo.dificuldade import Dificuldade

from views.tela_do_jogo import TelaDoJogo
from views.tela_inicial import TelaInicial

tela = Tk()


@pytest.mark.parametrize("linhas, colunas, esperado", [
    (8, 2, 64), (9, 8, 64), (1, 8, 64), (3, 8, 64),
    (8, 2, 64), (8, 5, 64), (8, 4, 64), (8, 3, 64),
    (8, 10, 64), (8, 15, 64), (10, 8, 64)
])
def testar_dimensoes_invalidas_facil(linhas, colunas, esperado):
    t = TelaDoJogo(8, 8, 10, tela)
    valido = False
    area = 0

    for l in range(linhas):
        for c in range(colunas):
            area += 1

    if t.linhas == linhas and t.colunas == colunas:
        if area == esperado:
            valido = True

    assert valido == False

@pytest.mark.parametrize("linhas, colunas, esperado", [
    (10, 15, 160), (12, 10, 160), (1, 10, 160), (3, 10, 160),
    (10, 10, 160), (10, 17, 160), (10, 13, 160), (10, 3, 160),
    (10, 2, 160), (10, 11, 160), (10, 18, 160)
])
def testar_dimensoes_invalidas_intermediario(linhas, colunas, esperado):
    t = TelaDoJogo(10, 16, 30, tela)
    valido = False
    area = 0

    for l in range(linhas):
        for c in range(colunas):
            area += 1

    if t.linhas == linhas and t.colunas == colunas:
        if area == esperado:
            valido = True

    assert valido == False

@pytest.mark.parametrize("linhas, colunas, esperado", [
    (24, 21, 576), (9, 4, 576), (1, 26, 576), (3, 20, 576),
    (18, 2, 576), (24, 10, 576), (24, 4, 576), (24, 3, 576),
    (22, 10, 576), (24, 15, 576), (10, 14, 576)
])
def testar_dimensoes_invalidas_dificil(linhas, colunas, esperado):
    t = TelaDoJogo(8, 8, 10, tela)
    valido = False
    area = 0

    for l in range(linhas):
        for c in range(colunas):
            area += 1

    if t.linhas == linhas and t.colunas == colunas:
        if area == esperado:
            valido = True

    assert valido == False

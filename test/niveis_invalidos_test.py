from tkinter import Tk
import pytest
from jogo.dificuldade import Dificuldade

from views.tela_do_jogo import TelaDoJogo
from views.tela_inicial import TelaInicial

tela = Tk()


@pytest.mark.parametrize("nivelInvalido, esperado", [
    ('fac', 'fácil'), ('faciil', 'fácil'), ('FACIL', 'fácil'), ('ffacil', 'fácil'),
    ('Facil', 'fácil'), ('Faacil', 'fácil'), ('Facíl', 'fácil'), ('Fail', 'fácil'),
    ('facii', 'fácil'), ('faccil', 'fácil'),
])

def testar_nivel_invalido_facil(nivelInvalido, esperado):
    valido = False

    TelaInicial.dificuldade = nivelInvalido

    d = Dificuldade(esperado)

    if TelaInicial.dificuldade == d.escolherNivel():
        valido = True

    assert valido == False


@pytest.mark.parametrize("nivelInvalido, esperado", [
    ('int', 'intermediário'), ('intermedia', 'intermediário'), ('INTERMEDIARIO', 'intermediário'), ('médio', 'intermediário'),
    ('intermediario', 'intermediário'), ('intermedio', 'intermediário'), ('Intermediario', 'intermediário'), ('INtermediario', 'intermediário'),
    ('inTermediar', 'intermediário'), ('Intermediário', 'intermediário'),
])

def testar_nivel_invalido_intermediario(nivelInvalido, esperado):
    valido = False

    TelaInicial.dificuldade = nivelInvalido

    d = Dificuldade(esperado)

    if TelaInicial.dificuldade == d.escolherNivel():
        valido = True

    assert valido == False


@pytest.mark.parametrize("nivelInvalido, esperado", [
    ('dif', 'difícil'), ('diifil', 'difícil'), ('DIFICIL', 'difícil'), ('Dificil', 'difícil'),
    ('Difiicil', 'difícil'), ('dificill', 'difícil'), ('díficil', 'difícil'), ('Difficil', 'difícil'),
    ('Dificil', 'difícil'), ('Dific', 'difícil'),
])

def testar_nivel_invalido_dificil(nivelInvalido, esperado):
    valido = False

    TelaInicial.dificuldade = nivelInvalido

    d = Dificuldade(esperado)

    if TelaInicial.dificuldade == d.escolherNivel():
        valido = True

    assert valido == False

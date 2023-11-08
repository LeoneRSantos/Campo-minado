from tkinter import Tk
import pytest
from jogo.dificuldade import Dificuldade
from views.tela_inicial import TelaInicial

tela = Tk()


@pytest.mark.parametrize("nivelInvalido, esperado", [
    ('fac124', 'fácil'), ('faciil', 'fácil'), ('FACIL', 'fácil'), ('ffacil', 'fácil'),
    ('1234', 'fácil'), ('Faacil', 'fácil'), ('Fa...cíl', 'fácil'), ('Fail', 'fácil'),
    ('faci3i', 'fácil'), ('fa#ccil', 'fácil'),
])

def testar_nivel_invalido_facil(nivelInvalido, esperado):
    valido = False

    TelaInicial.dificuldade = nivelInvalido

    d = Dificuldade(esperado)

    if TelaInicial.dificuldade == d.escolherNivel():
        valido = True

    assert valido == False


@pytest.mark.parametrize("nivelInvalido, esperado", [
    ('int1', 'intermediário'), ('intermedia', 'intermediário'), ('INTERMED#IARIO', 'intermediário'), ('médio', 'intermediário'),
    ('interm23.iario', 'intermediário'), ('int@ermedio', 'intermediário'), ('Intermediario', 'intermediário'), ('INtermediario', 'intermediário'),
    ('inTermediar10', 'intermediário'), ('Inte23rmediário', 'intermediário'),
])

def testar_nivel_invalido_intermediario(nivelInvalido, esperado):
    valido = False

    TelaInicial.dificuldade = nivelInvalido

    d = Dificuldade(esperado)

    if TelaInicial.dificuldade == d.escolherNivel():
        valido = True

    assert valido == False


@pytest.mark.parametrize("nivelInvalido, esperado", [
    ('dif@', 'difícil'), ('diifil', 'difícil'), ('DIFICIL', 'difícil'), ('Dificil', 'difícil'),
    ('Difii$cil', 'difícil'), ('dif21icill', 'difícil'), ('díficil', 'difícil'), ('Difficil', 'difícil'),
    ('Dif#5icil', 'difícil'), ('Di;.fic', 'difícil'),
])

def testar_nivel_invalido_dificil(nivelInvalido, esperado):
    valido = False

    TelaInicial.dificuldade = nivelInvalido

    d = Dificuldade(esperado)

    if TelaInicial.dificuldade == d.escolherNivel():
        valido = True

    assert valido == False

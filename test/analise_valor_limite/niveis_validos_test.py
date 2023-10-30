import pytest
from jogo.dificuldade import Dificuldade

from views.tela_inicial import TelaInicial


@pytest.mark.parametrize("nivelValido, esperado", [ 
    ('fácil','fácil'),
    ('intermediário','intermediário'),
    ('difícil', 'difícil')
])
def testar_niveis_validos(nivelValido, esperado):
    valido = True

    TelaInicial.dificuldade = nivelValido

    d = Dificuldade(esperado)

    if TelaInicial.dificuldade != d.escolherNivel():
        valido = False

    assert valido == True
from jogo.dificuldade import Dificuldade
from main import main

def testeNivelAEscolher(): 
    assert Dificuldade.nivel == ''

def testeNivelEscolhido():
    assert main != ''

def testeEscolherNivelFacil(): 
    d = Dificuldade('fácil')

    assert d.escolherNivel() == 'fácil'

def testeEscolherFacilPeloClique():
    d = Dificuldade('fácil') 

    TelaInicial.dificuldade = 'fácil'

    assert d.nivel == TelaInicial.dificuldade

def testeEscolherInterPeloClique():
    d = Dificuldade('intermediário') 

    TelaInicial.dificuldade = 'intermediário'

    assert d.nivel == TelaInicial.dificuldade


def testeEscolherDificilPeloClique():
    d = Dificuldade('difícil') 

    TelaInicial.dificuldade = 'difícil'

    assert d.nivel == TelaInicial.dificuldade


def testeEscolherNivelIntermediário(): 
    d = Dificuldade('intermediário')

    assert d.escolherNivel() == 'intermediário'

def testeEscolherNiveDificil(): 
    d = Dificuldade('difícil')

    assert d.escolherNivel() == 'difícil'
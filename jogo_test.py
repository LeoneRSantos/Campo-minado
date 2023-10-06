from jogo.dificuldade import Dificuldade
from main import main

def testeNivelAEscolher(): 
    assert Dificuldade.nivel == ''

def testeNivelEscolhido():
    assert main != ''

def testeEscolherNivelFacil(): 
    d = Dificuldade('fácil')

    assert d.escolherNivel() == 'fácil'

def testeEscolherNivelIntermediário(): 
    d = Dificuldade('intermediário')

    assert d.escolherNivel() == 'intermediário'

def testeEscolherNiveDificil(): 
    d = Dificuldade('difícil')

    assert d.escolherNivel() == 'difícil'